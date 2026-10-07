# 🎥 Pipeline de edição — vídeo talking-head

Fluxo para transformar uma gravação sua (você falando para a câmera) em um Reel/Short pronto.

> **Transparência sobre o que dá pra automatizar:** edição talking-head de verdade (cortar silêncios,
> legenda queimada, formato 9:16, trilha) pode ser **90% automatizada com FFmpeg + Whisper** aqui mesmo.
> O que ainda é seu: a gravação, a escolha de takes e o ajuste fino de ritmo. Abaixo o pipeline que eu rodo pra você.

---

## Etapas

### 1. Entrada
Você me dá o arquivo de vídeo (coloque em `04-producao-video/raw/`). Ideal: gravado na horizontal ou já vertical, boa luz e áudio.

### 2. Transcrição + legenda automática (Whisper)
Gero a transcrição com marcação de tempo e um arquivo `.srt` em português.
→ serve para legenda queimada **e** para revisar o que você falou.

### 3. Cortes automáticos
- Remoção de silêncios/pausas longas (deixa o vídeo mais dinâmico).
- Corte de "ééé", repetições e erros marcados por você ("corta daqui até aqui").

### 4. Formatação 9:16
- Reenquadra para vertical, com você centralizado.
- Opcional: fundo/barra superior e inferior com título do vídeo.

### 5. Legenda na tela (estilo Reels)
- Legenda queimada, palavra destacada, fonte grande e legível sem som.

### 6. Toques finais
- Trilha/áudio em alta (respeitando direitos).
- Capa/primeiro frame com gancho.
- Exporto em MP4 pronto para postar → `04-producao-video/pronto/`.

---

## Ferramentas do pipeline (abertas, rodam aqui)
- **FFmpeg** — cortes, reenquadre 9:16, legenda queimada, trilha, export.
- **Whisper** (openai-whisper / faster-whisper) — transcrição e geração de `.srt`.
- **auto-editor** (opcional) — remoção automática de silêncios.

> Se alguma não estiver instalada no ambiente, eu instalo na hora de usar.

## Pastas
```
04-producao-video/
├── raw/      ← seus vídeos crus (entram aqui)
├── legendas/ ← .srt e transcrições
└── pronto/   ← MP4 final pra postar
```

## Como pedir
*"Edita esse vídeo talking-head: legenda em PT, corta os silêncios, 9:16, com o título X na capa."*
Me diga a duração-alvo e o estilo de legenda; eu rodo o pipeline e te entrego o MP4.

> **Ferramentas de edição assistida por IA mais avançadas** (CapCut, Descript, Opus Clip) fazem partes disso com
> interface visual — posso gerar o roteiro/legenda/cortes aqui e você finaliza nelas, se preferir. É só dizer o seu fluxo.
