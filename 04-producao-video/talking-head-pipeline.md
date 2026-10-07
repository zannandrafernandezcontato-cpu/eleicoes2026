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
> **Já instaladas e testadas aqui:** ffmpeg 6.1.1, auto-editor 29.3.1, faster-whisper 1.2.1.

### ⚠️ Nota sobre a transcrição automática neste ambiente
O reenquadre 9:16, o título, a legenda queimada e o corte de silêncios rodam **100% offline**.
Já a **transcrição automática** (Whisper) precisa baixar o modelo uma vez, e a política de rede
deste ambiente cloud **bloqueia o host do modelo (HuggingFace)**. Opções:
1. Rodar o pipeline **com uma legenda `.srt` pronta** (`--srt arquivo.srt`) — funciona perfeitamente.
2. Liberar os hosts de modelo nas configurações de rede do ambiente cloud (menu do ambiente na barra
   de título → **Edit** → *Network access*): use um nível de acesso mais amplo, ou adicione em
   *Allowed domains* os hosts **`huggingface.co`** e **`cdn-lfs.huggingface.co`** (deixe marcada a
   caixa que inclui os gerenciadores de pacote). Guia: https://code.claude.com/docs/en/cloud-environments#network-access
   Isso libera a transcrição automática **e** as APIs de busca de imagem.
3. Rodar a transcrição na sua máquina (sem esse bloqueio) e trazer o `.srt`.

### ⭐ Legenda sem transcrição (solução offline, recomendada aqui)
Como você trabalha com **roteiro**, dá pra pular o Whisper: a legenda sai do próprio texto que você leu.
- **`scripts/roteiro_para_srt.py`** — recebe o texto falado + a duração do vídeo e gera o `.srt`
  com tempos proporcionais. Ex.: `python3 scripts/roteiro_para_srt.py narracao.txt 58 narracao.srt`
- Depois roda o pipeline com `--srt narracao.srt`. Zero dependência de rede.
- Fluxo: grave lendo o roteiro → me diga a duração → eu gero a legenda → Reel pronto (ajuste fino no editor, se quiser).

### Scripts do pipeline
- **`scripts/edita_talking_head.sh`** — orquestra tudo. Ex.:
  `scripts/edita_talking_head.sh raw/meu_video.mp4 --titulo "Esquerda x Direita"`
- **`scripts/roteiro_para_srt.py`** — legenda a partir do roteiro (offline). **Recomendado neste ambiente.**
- **`scripts/transcrever.py`** — legenda por transcrição automática (Whisper). Requer liberar a rede (abaixo).

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
