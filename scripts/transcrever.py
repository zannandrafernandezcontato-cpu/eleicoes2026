#!/usr/bin/env python3
"""Transcreve um vídeo/áudio em português e gera legenda .srt (faster-whisper).

Uso: python3 transcrever.py <entrada> <saida.srt> [modelo]
  modelo: tiny | base | small (padrão) | medium  — maior = mais preciso e mais lento
"""
import sys


def fmt(t: float) -> str:
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = int(t % 60)
    ms = int(round((t - int(t)) * 1000))
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def main() -> None:
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    entrada, saida = sys.argv[1], sys.argv[2]
    modelo = sys.argv[3] if len(sys.argv) > 3 else "small"

    from faster_whisper import WhisperModel

    model = WhisperModel(modelo, device="cpu", compute_type="int8")
    segments, _info = model.transcribe(entrada, language="pt", vad_filter=True)

    with open(saida, "w", encoding="utf-8") as f:
        for i, seg in enumerate(segments, 1):
            f.write(f"{i}\n{fmt(seg.start)} --> {fmt(seg.end)}\n{seg.text.strip()}\n\n")
    print(f"✅ Legenda salva em {saida}")


if __name__ == "__main__":
    main()
