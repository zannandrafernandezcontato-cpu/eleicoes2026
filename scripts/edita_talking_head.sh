#!/usr/bin/env bash
# Pipeline de edição talking-head -> Reel/Short vertical 9:16 com legenda em PT.
#
# Uso:
#   scripts/edita_talking_head.sh ENTRADA [opções]
# Opções:
#   --titulo "Texto"   Faixa de título no topo do vídeo
#   --modelo small     Modelo de transcrição (tiny|base|small|medium) [padrão: small]
#   --srt arquivo.srt  Usa uma legenda pronta (pula a transcrição)
#   --sem-legenda      Não queima legenda
#   --sem-cortes       Não remove silêncios (pula o auto-editor)
#   --saida arquivo    Caminho do MP4 final [padrão: 04-producao-video/pronto/<nome>_reel.mp4]
#
# Requer: ffmpeg, (faster-whisper via scripts/transcrever.py), auto-editor (opcional)
set -euo pipefail

AQUI="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENTRADA="${1:?Informe o arquivo de vídeo de entrada}"; shift || true

TITULO=""; MODELO="small"; SRT=""; LEGENDA=1; CORTES=1; SAIDA=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --titulo) TITULO="$2"; shift 2;;
    --modelo) MODELO="$2"; shift 2;;
    --srt) SRT="$2"; LEGENDA=1; shift 2;;
    --sem-legenda) LEGENDA=0; shift;;
    --sem-cortes) CORTES=0; shift;;
    --saida) SAIDA="$2"; shift 2;;
    *) echo "Opção desconhecida: $1" >&2; exit 1;;
  esac
done

BASE="$(basename "${ENTRADA%.*}")"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
mkdir -p "$AQUI/04-producao-video/pronto" "$AQUI/04-producao-video/legendas"
[[ -z "$SAIDA" ]] && SAIDA="$AQUI/04-producao-video/pronto/${BASE}_reel.mp4"

FONTE="$ENTRADA"

# 1) Remoção de silêncios (opcional)
if [[ "$CORTES" -eq 1 ]] && command -v auto-editor >/dev/null 2>&1; then
  echo "✂️  Removendo silêncios (auto-editor)..."
  auto-editor "$FONTE" --no-open -o "$TMP/cortado.mp4" >/dev/null 2>&1 && FONTE="$TMP/cortado.mp4" || echo "   (auto-editor falhou; seguindo sem cortes)"
fi

# 2) Transcrição -> SRT (a menos que já tenha sido passado)
if [[ "$LEGENDA" -eq 1 && -z "$SRT" ]]; then
  echo "📝 Transcrevendo (modelo: $MODELO)..."
  SRT="$AQUI/04-producao-video/legendas/${BASE}.srt"
  python3 "$AQUI/scripts/transcrever.py" "$FONTE" "$SRT" "$MODELO"
fi

# 3) Monta o filtro: fundo borrado 9:16 + vídeo centralizado + (título) + (legenda)
FILTRO="[0:v]split=2[bg][fg];\
[bg]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,gblur=sigma=20[bgb];\
[fg]scale=1080:-2[fgs];\
[bgb][fgs]overlay=(W-w)/2:(H-h)/2[base]"

LAST="base"
if [[ -n "$TITULO" ]]; then
  TSAFE="${TITULO//\'/\\\'}"
  FILTRO="$FILTRO;[${LAST}]drawtext=text='${TSAFE}':fontcolor=white:fontsize=52:box=1:boxcolor=black@0.55:boxborderw=22:x=(w-text_w)/2:y=150[titled]"
  LAST="titled"
fi
if [[ "$LEGENDA" -eq 1 && -n "$SRT" && -f "$SRT" ]]; then
  SRTE="${SRT//\'/\\\'}"
  FILTRO="$FILTRO;[${LAST}]subtitles='${SRTE}':force_style='FontName=DejaVu Sans,Fontsize=16,Bold=1,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BorderStyle=1,Outline=4,Shadow=0,Alignment=2,MarginV=260'[out]"
  LAST="out"
fi

echo "🎞️  Renderizando 9:16 -> $SAIDA"
ffmpeg -y -i "$FONTE" -filter_complex "$FILTRO" -map "[$LAST]" -map 0:a? \
  -c:v libx264 -preset veryfast -crf 20 -pix_fmt yuv420p -c:a aac -b:a 128k \
  "$SAIDA" >/dev/null 2>&1

echo "✅ Pronto: $SAIDA"
