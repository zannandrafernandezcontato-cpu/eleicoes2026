#!/usr/bin/env python3
"""Gera o painel (dashboard) do sistema a partir do conteúdo do repositório.

Lê: 00-marca/marca.json, último briefing, banco de pautas, roteiros.
Escreve: painel/index.html — página única, offline, mobile-first, na sua marca.

Uso: python3 scripts/gera_painel.py
"""
import glob
import html
import json
import os
import re
from datetime import date, datetime

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SEGUNDO_TURNO = date(2026, 10, 25)  # ajuste conforme o calendário

DEF_CORES = {
    "fundo": "#0F1B2D", "fundo_card": "#16263E", "texto": "#F0F4FA",
    "texto_secundario": "#96A5B9", "destaque": "#FFD24C",
    "neutro_a": "#5AC8BE", "neutro_b": "#F5A05A",
}


def carrega_marca():
    try:
        with open(os.path.join(BASE, "00-marca", "marca.json"), encoding="utf-8") as f:
            m = json.load(f)
        return {**DEF_CORES, **m.get("cores", {})}, m.get("handle", "@seu_perfil")
    except Exception:
        return DEF_CORES, "@seu_perfil"


def ultimo_briefing():
    arqs = sorted(glob.glob(os.path.join(BASE, "00-inteligencia", "briefings", "*.md")))
    if not arqs:
        return None, None, []
    caminho = arqs[-1]
    with open(caminho, encoding="utf-8") as f:
        txt = f.read()
    # título (primeira linha # ...) e bullets da 1a seção de conteúdo
    titulo = next((l.lstrip("# ").strip() for l in txt.splitlines() if l.startswith("#")), "Briefing")
    bullets = []
    dentro = False
    for l in txt.splitlines():
        if re.match(r"^##\s", l):
            dentro = "quente" in l.lower() or "1." in l
            continue
        if dentro and l.strip().startswith("- "):
            bullets.append(re.sub(r"\*\*(.+?)\*\*", r"\1", l.strip()[2:]))
        elif dentro and bullets and re.match(r"^##\s", l):
            break
    return titulo, os.path.relpath(caminho, BASE), bullets[:5]


def conta_secao(txt, nome):
    """Conta linhas de tabela (pautas) dentro de uma seção '## ... nome ...'."""
    linhas = txt.splitlines()
    cap, itens = False, []
    for l in linhas:
        if re.match(r"^##\s", l):
            cap = nome.lower() in l.lower()
            continue
        if cap and l.strip().startswith("|"):
            cels = [c.strip() for c in l.strip().strip("|").split("|")]
            if not cels or set("".join(cels)) <= set("-: "):
                continue
            if cels[0].lower() in ("#", "data"):
                continue
            # pega a coluna que parece o nome da pauta (2a célula normalmente)
            nome_pauta = cels[1] if len(cels) > 1 else cels[0]
            if nome_pauta and nome_pauta.lower() != "pauta":
                itens.append(nome_pauta)
    return itens


def pautas():
    caminho = os.path.join(BASE, "01-pautas", "banco-de-pautas.md")
    try:
        with open(caminho, encoding="utf-8") as f:
            txt = f.read()
    except Exception:
        return [], [], []
    return (conta_secao(txt, "Aprovadas"), conta_secao(txt, "A avaliar"),
            conta_secao(txt, "Publicadas"))


def roteiros():
    out = []
    for p in sorted(glob.glob(os.path.join(BASE, "02-roteiros", "*.md"))):
        if os.path.basename(p).lower() == "readme.md":
            continue
        nome = os.path.basename(p)
        titulo = nome
        try:
            with open(p, encoding="utf-8") as f:
                for l in f:
                    if l.startswith("#"):
                        titulo = l.lstrip("# ").strip()
                        break
        except Exception:
            pass
        out.append((titulo, os.path.relpath(p, BASE)))
    return out


def chip(txt, cor, fundo):
    return f'<span class="chip" style="color:{cor};border-color:{cor};">{html.escape(txt)}</span>'


def li(txt, href=None):
    t = html.escape(txt)
    if href:
        return f'<li><a href="../{html.escape(href)}">{t}</a></li>'
    return f"<li>{t}</li>"


def main():
    cores, handle = carrega_marca()
    btitulo, bpath, bullets = ultimo_briefing()
    aprov, avaliar, public = pautas()
    rots = roteiros()

    dias = (SEGUNDO_TURNO - date.today()).days
    if dias > 0:
        contagem = f"{dias} dias para o 2º turno (25/10)"
    elif dias == 0:
        contagem = "Hoje é o 2º turno!"
    else:
        contagem = "Período pós-eleição"

    atualizado = datetime.now().strftime("%d/%m/%Y %H:%M")

    bl = "".join(f"<li>{html.escape(b)}</li>" for b in bullets) or "<li>Rode o briefing do dia.</li>"
    aprov_li = "".join(li(x) for x in aprov) or "<li class='vazio'>nenhuma aprovada</li>"
    avaliar_li = "".join(li(x) for x in avaliar) or "<li class='vazio'>banco vazio</li>"
    rots_li = "".join(li(t, h) for t, h in rots) or "<li class='vazio'>nenhum roteiro ainda</li>"
    brief_link = f'<a class="link" href="../{html.escape(bpath)}">abrir briefing completo →</a>' if bpath else ""

    pag = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Painel · Conteúdo Eleições 2026</title>
<style>
  :root {{
    --bg:{cores['fundo']}; --card:{cores['fundo_card']}; --ink:{cores['texto']};
    --mute:{cores['texto_secundario']}; --accent:{cores['destaque']};
    --a:{cores['neutro_a']}; --b:{cores['neutro_b']};
  }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--bg); color:var(--ink);
    font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
    line-height:1.5; }}
  header {{ padding:28px 20px 20px; border-bottom:1px solid rgba(255,255,255,.08);
    position:sticky; top:0; background:var(--bg); z-index:10; }}
  h1 {{ margin:0; font-size:20px; letter-spacing:.2px; }}
  .sub {{ color:var(--mute); font-size:13px; margin-top:6px; }}
  .countdown {{ display:inline-block; margin-top:12px; padding:8px 14px; border-radius:999px;
    background:var(--accent); color:var(--bg); font-weight:700; font-size:14px; }}
  main {{ padding:20px; max-width:1100px; margin:0 auto;
    display:grid; grid-template-columns:repeat(auto-fit,minmax(300px,1fr)); gap:16px; }}
  .card {{ background:var(--card); border-radius:16px; padding:20px 22px;
    border:1px solid rgba(255,255,255,.06); }}
  .card h2 {{ margin:0 0 12px; font-size:15px; text-transform:uppercase;
    letter-spacing:1px; color:var(--accent); }}
  ul {{ margin:0; padding-left:18px; }}
  li {{ margin:7px 0; }}
  li.vazio {{ color:var(--mute); list-style:none; margin-left:-18px; font-style:italic; }}
  a {{ color:var(--ink); text-decoration:none; border-bottom:1px solid rgba(255,255,255,.2); }}
  a:hover {{ border-color:var(--accent); color:var(--accent); }}
  .link {{ display:inline-block; margin-top:14px; color:var(--accent); border:0; font-weight:600; }}
  .nums {{ display:flex; gap:22px; margin-bottom:8px; }}
  .num b {{ font-size:28px; color:var(--accent); display:block; }}
  .num span {{ font-size:12px; color:var(--mute); }}
  .chip {{ display:inline-block; padding:2px 10px; border:1px solid; border-radius:999px;
    font-size:12px; margin:2px 4px 2px 0; }}
  footer {{ color:var(--mute); font-size:12px; text-align:center; padding:28px 20px 40px; }}
  .full {{ grid-column:1/-1; }}
</style>
</head>
<body>
<header>
  <h1>🗳️ Painel de Conteúdo · Eleições 2026</h1>
  <div class="sub">{handle} · atualizado em {atualizado}</div>
  <div class="countdown">⏳ {contagem}</div>
</header>
<main>
  <section class="card full">
    <h2>📊 {html.escape(btitulo or 'Briefing do dia')}</h2>
    <ul>{bl}</ul>
    {brief_link}
  </section>

  <section class="card">
    <h2>🗂️ Banco de Pautas</h2>
    <div class="nums">
      <div class="num"><b>{len(avaliar)}</b><span>a avaliar</span></div>
      <div class="num"><b>{len(aprov)}</b><span>aprovadas</span></div>
      <div class="num"><b>{len(public)}</b><span>publicadas</span></div>
    </div>
    <strong style="font-size:13px;color:var(--mute)">Aprovadas</strong>
    <ul>{aprov_li}</ul>
    <strong style="font-size:13px;color:var(--mute)">A avaliar</strong>
    <ul>{avaliar_li}</ul>
  </section>

  <section class="card">
    <h2>🎬 Roteiros prontos</h2>
    <ul>{rots_li}</ul>
  </section>

  <section class="card full">
    <h2>🧭 Fluxo do sistema</h2>
    <p style="color:var(--mute);margin:0">
      {chip('Pesquisa', cores['neutro_a'], cores['fundo'])}→
      {chip('Pautas', cores['destaque'], cores['fundo'])}→
      {chip('Roteiro', cores['neutro_b'], cores['fundo'])}→
      {chip('Produção', cores['neutro_a'], cores['fundo'])}→
      {chip('Resultados', cores['destaque'], cores['fundo'])}
      — os resultados realimentam as pautas.
    </p>
  </section>
</main>
<footer>Gerado automaticamente a partir do repositório · reconstruído pela rotina diária</footer>
</body>
</html>"""

    saida = os.path.join(BASE, "painel")
    os.makedirs(saida, exist_ok=True)
    with open(os.path.join(saida, "index.html"), "w", encoding="utf-8") as f:
        f.write(pag)
    print(f"✅ Painel gerado em painel/index.html "
          f"({len(avaliar)} a avaliar, {len(aprov)} aprovadas, {len(rots)} roteiros)")


if __name__ == "__main__":
    main()
