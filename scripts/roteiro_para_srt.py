#!/usr/bin/env python3
"""Gera legenda .srt a partir do TEXTO do roteiro — sem transcrição/Whisper.

Ideal para vídeo roteirizado (você lê o que escreveu). Distribui o tempo
proporcional ao nº de palavras de cada trecho, dentro da duração total do vídeo.
Depois é só ajustar finamente no editor, se precisar.

Uso:
  python3 roteiro_para_srt.py <roteiro.txt> <duracao_seg> <saida.srt>
  # roteiro.txt: o texto falado (parágrafos ou uma frase por linha)
  # duracao_seg: duração real do vídeo gravado (ex.: 58)
"""
import re
import sys


def fmt(t: float) -> str:
    h = int(t // 3600); m = int((t % 3600) // 60); s = int(t % 60)
    ms = int(round((t - int(t)) * 1000))
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def chunk(texto, max_chars=42):
    """Quebra o texto em trechos curtos de legenda (~2 linhas de até 42 chars)."""
    # separa por frases, depois agrupa até o limite
    frases = re.split(r"(?<=[\.\!\?\:\;])\s+", texto.strip())
    trechos, atual = [], ""
    for fr in frases:
        fr = fr.strip()
        if not fr:
            continue
        if len(fr) <= max_chars * 2:
            if atual and len(atual) + len(fr) + 1 <= max_chars * 2:
                atual = f"{atual} {fr}"
            else:
                if atual:
                    trechos.append(atual)
                atual = fr
        else:
            # frase longa: quebra por palavras
            if atual:
                trechos.append(atual); atual = ""
            palavras, linha = fr.split(), ""
            for p in palavras:
                if len(linha) + len(p) + 1 <= max_chars * 2:
                    linha = f"{linha} {p}".strip()
                else:
                    trechos.append(linha); linha = p
            if linha:
                atual = linha
    if atual:
        trechos.append(atual)
    return trechos


def duas_linhas(t, max_chars=42):
    if len(t) <= max_chars:
        return t
    palavras, l1, l2 = t.split(), "", ""
    for p in palavras:
        if len(l1) + len(p) + 1 <= max_chars and not l2:
            l1 = f"{l1} {p}".strip()
        else:
            l2 = f"{l2} {p}".strip()
    return f"{l1}\n{l2}".strip()


def main():
    if len(sys.argv) < 4:
        print(__doc__); sys.exit(1)
    with open(sys.argv[1], encoding="utf-8") as f:
        texto = f.read()
    dur = float(sys.argv[2]); saida = sys.argv[3]

    trechos = chunk(texto)
    pesos = [max(1, len(t.split())) for t in trechos]
    total = sum(pesos)
    t0 = 0.0
    with open(saida, "w", encoding="utf-8") as f:
        for i, (tr, w) in enumerate(zip(trechos, pesos), 1):
            t1 = t0 + dur * (w / total)
            f.write(f"{i}\n{fmt(t0)} --> {fmt(min(t1, dur))}\n{duas_linhas(tr)}\n\n")
            t0 = t1
    print(f"✅ {len(trechos)} legendas em {saida} (duração {dur:.0f}s). Ajuste fino no editor se precisar.")


if __name__ == "__main__":
    main()
