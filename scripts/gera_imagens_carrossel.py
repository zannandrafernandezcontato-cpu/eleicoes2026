#!/usr/bin/env python3
"""Gera as artes de um carrossel (1080x1350, 4:5) com Pillow — sem banco de imagem.

Artes 100% originais (licença sua), tom neutro (sem cores partidárias).
Uso: python3 gera_imagens_carrossel.py [pasta_saida]
"""
import os
import sys
from PIL import Image, ImageDraw, ImageFont

# ---- Identidade visual (ajuste à sua marca) ----
W, H = 1080, 1350
BG = (15, 27, 45)          # navy profundo
BG2 = (22, 38, 62)         # navy mais claro (cards de conteúdo)
INK = (240, 244, 250)      # texto claro
ACCENT = (255, 210, 76)    # amarelo destaque
MUTE = (150, 165, 185)     # texto secundário
NEUTRO_A = (90, 200, 190)  # teal (polo A, neutro)
NEUTRO_B = (245, 160, 90)  # âmbar (polo B, neutro)
MARGIN = 96
FONTE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONTE_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def fnt(sz, bold=True):
    return ImageFont.truetype(FONTE_B if bold else FONTE, sz)


def wrap(draw, text, font, max_w):
    linhas, atual = [], ""
    for palavra in text.split():
        teste = (atual + " " + palavra).strip()
        if draw.textlength(teste, font=font) <= max_w:
            atual = teste
        else:
            if atual:
                linhas.append(atual)
            atual = palavra
    if atual:
        linhas.append(atual)
    return linhas


def desenha_texto(draw, xy, text, font, fill, max_w, leading=1.28):
    x, y = xy
    alt = font.size * leading
    for ln in wrap(draw, text, font, max_w):
        draw.text((x, y), ln, font=font, fill=fill)
        y += alt
    return y


def pill(draw, xy, text, font, fill_bg, fill_tx):
    x, y = xy
    tw = draw.textlength(text, font=font)
    pad_x, pad_y = 28, 16
    draw.rounded_rectangle([x, y, x + tw + pad_x * 2, y + font.size + pad_y * 2],
                           radius=(font.size + pad_y * 2) // 2, fill=fill_bg)
    draw.text((x + pad_x, y + pad_y), text, font=font, fill=fill_tx)
    return y + font.size + pad_y * 2


def rodape(draw, n, total, handle="@seu_perfil"):
    y = H - 70
    draw.text((MARGIN, y), handle, font=fnt(28, False), fill=MUTE)
    # pontinhos de progresso
    cx = W - MARGIN - total * 26
    for i in range(total):
        cor = ACCENT if i == n - 1 else (60, 76, 100)
        draw.ellipse([cx + i * 26, y + 6, cx + i * 26 + 14, y + 20], fill=cor)


def regua(draw, y, rot_esq, rot_dir, titulo):
    """Barra horizontal neutra (gradiente teal->âmbar) com rótulos nos polos."""
    y = int(y)
    draw.text((MARGIN, y - 54), titulo, font=fnt(34), fill=ACCENT)
    x0, x1 = MARGIN, W - MARGIN
    h = 44
    bar = Image.new("RGB", (x1 - x0, h))
    bp = bar.load()
    for ix in range(x1 - x0):
        t = ix / (x1 - x0)
        bp[ix, 0] = tuple(int(NEUTRO_A[k] + (NEUTRO_B[k] - NEUTRO_A[k]) * t) for k in range(3))
    for iy in range(1, h):
        for ix in range(x1 - x0):
            bp[ix, iy] = bp[ix, 0]
    mask = Image.new("L", (x1 - x0, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, x1 - x0 - 1, h - 1], radius=h // 2, fill=255)
    draw._image.paste(bar, (x0, y), mask)
    f = fnt(26, False)
    draw.text((x0, y + h + 14), rot_esq, font=f, fill=INK)
    tw = draw.textlength(rot_dir, font=f)
    draw.text((x1 - tw, y + h + 14), rot_dir, font=f, fill=INK)


# ---- Conteúdo do carrossel "Esquerda e direita" ----
CARDS = [
    {"tipo": "capa", "titulo": "Esquerda e direita: o que isso quer dizer, afinal?",
     "apoio": "Sem torcida. Só o conceito, pra você formar sua opinião."},
    {"tipo": "texto", "kicker": "De onde vem", "corpo":
     "Os termos nasceram na Revolução Francesa (1789). Na assembleia, quem queria mudar a ordem "
     "sentava à esquerda; quem queria conservar, à direita. A geografia virou vocabulário político."},
    {"tipo": "quadrante", "kicker": "Não é uma linha só",
     "corpo": "Dá pra pensar em dois eixos ao mesmo tempo: economia e costumes."},
    {"tipo": "regua", "kicker": "Eixo 1 — economia",
     "titulo": "Papel do Estado", "esq": "Mais Estado", "dir": "Mais mercado",
     "corpo": "Mais à esquerda: Estado atua mais (impostos, serviços, redução da desigualdade). "
              "Mais à direita: mercado atua mais (menos Estado, menos impostos)."},
    {"tipo": "regua", "kicker": "Eixo 2 — costumes",
     "titulo": "Valores e sociedade", "esq": "Progressista", "dir": "Conservador",
     "corpo": "Progressista: prioriza mudanças e novos direitos. Conservador: prioriza tradição e "
              "instituições. Esse eixo nem sempre anda junto com o econômico."},
    {"tipo": "texto", "kicker": "Entre os extremos",
     "corpo": "Existe centro, centro-esquerda, centro-direita. A maioria fica nas faixas do meio, "
              "misturando posições. Rótulo fechado quase sempre simplifica demais."},
    {"tipo": "texto", "kicker": "Por que confunde",
     "corpo": "Os termos mudam conforme o país e a época, e viram ofensa. Entender os eixos ajuda a "
              "enxergar a proposta concreta por trás do apelido."},
    {"tipo": "texto", "kicker": "O teste que vale",
     "corpo": "Diante de qualquer político, pergunte: o que ele propõe sobre economia? E sobre "
              "costumes? As respostas dizem mais que o rótulo."},
    {"tipo": "cta", "titulo": "Olhe a proposta, não o rótulo.",
     "corpo": "Ninguém cabe 100% num lado — e tá tudo bem.",
     "cta": "Salva e manda pra alguém que precisa ver.",
     "fonte": "Fontes: Revolução Francesa (1789) · N. Bobbio, Direita e Esquerda (1994)"},
]


def render(card, n, total):
    bg = BG if card["tipo"] in ("capa", "cta") else BG2
    img = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(img)
    d._image = img
    maxw = W - 2 * MARGIN

    if card["tipo"] == "capa":
        d.rectangle([0, 0, 16, H], fill=ACCENT)
        y = 300
        y = desenha_texto(d, (MARGIN, y), card["titulo"], fnt(74), INK, maxw, 1.18)
        d.rounded_rectangle([MARGIN, y + 20, MARGIN + 110, y + 32], radius=6, fill=ACCENT)
        desenha_texto(d, (MARGIN, y + 70), card["apoio"], fnt(36, False), MUTE, maxw)
        d.text((W - MARGIN - 70, H - 180), "→", font=fnt(90), fill=ACCENT)

    elif card["tipo"] == "texto":
        y = 220
        y = pill(d, (MARGIN, y), card["kicker"], fnt(32), ACCENT, BG)
        desenha_texto(d, (MARGIN, y + 60), card["corpo"], fnt(52), INK, maxw, 1.32)

    elif card["tipo"] == "regua":
        y = 200
        y = pill(d, (MARGIN, y), card["kicker"], fnt(32), ACCENT, BG)
        y = desenha_texto(d, (MARGIN, y + 50), card["corpo"], fnt(40, False), INK, maxw, 1.3)
        regua(d, y + 90, card["esq"], card["dir"], card["titulo"])

    elif card["tipo"] == "quadrante":
        y = 180
        y = pill(d, (MARGIN, y), card["kicker"], fnt(32), ACCENT, BG)
        desenha_texto(d, (MARGIN, y + 46), card["corpo"], fnt(38, False), INK, maxw, 1.3)
        # eixos cruzados
        cx, cy, r = W // 2, 880, 300
        d.line([cx - r, cy, cx + r, cy], fill=MUTE, width=4)
        d.line([cx, cy - r, cx, cy + r], fill=MUTE, width=4)
        f = fnt(30)
        d.text((cx - r - 10, cy + 20), "Mais\nEstado", font=f, fill=NEUTRO_A)
        tw = d.textlength("Mais mercado", font=f)
        d.text((cx + r - tw + 10, cy + 20), "Mais\nmercado", font=f, fill=NEUTRO_B, align="right")
        d.text((cx + 20, cy - r - 10), "Progressista", font=f, fill=INK)
        d.text((cx + 20, cy + r - 30), "Conservador", font=f, fill=INK)

    elif card["tipo"] == "cta":
        d.rectangle([0, 0, 16, H], fill=ACCENT)
        y = 300
        y = desenha_texto(d, (MARGIN, y), card["titulo"], fnt(64), ACCENT, maxw, 1.2)
        y = desenha_texto(d, (MARGIN, y + 40), card["corpo"], fnt(44, False), INK, maxw)
        y = desenha_texto(d, (MARGIN, y + 60), card["cta"], fnt(44), INK, maxw)
        desenha_texto(d, (MARGIN, H - 240), card["fonte"], fnt(24, False), MUTE, maxw)

    rodape(d, n, total)
    return img


def main():
    saida = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(__file__), "..", "03-imagens", "gerado", "esquerda-e-direita")
    os.makedirs(saida, exist_ok=True)
    total = len(CARDS)
    for i, card in enumerate(CARDS, 1):
        img = render(card, i, total)
        caminho = os.path.join(saida, f"card-{i:02d}.png")
        img.save(caminho, "PNG")
        print(f"✅ {caminho}")
    print(f"\n{total} cards gerados em {saida}")


if __name__ == "__main__":
    main()
