# 🗳️ Sistema de Conteúdo — Eleições 2026

Sistema dinâmico de apoio à criação de conteúdo sobre as eleições de 2026.
Pensado para um creator que produz **Reels / TikTok / Shorts** e **carrosséis de Instagram**,
com linha editorial **análise + opinião + educação cívica** — plural, com fontes, mas com a sua leitura.

> **Momento atual (atualize conforme o calendário):** estamos **entre o 1º e o 2º turno**.
> 2º turno em **25/10/2026**. Este é o pico de atenção do público — o sistema está calibrado para esse momento.

---

## Como o sistema funciona (o fluxo)

```
   PESQUISA          →   PAUTAS         →   ROTEIRO        →   PRODUÇÃO        →   RESULTADOS
   (diária/auto)         (banco)            (Reel/carrossel)   (imagens/vídeo)     (métricas)
   00-inteligencia       01-pautas          02-roteiros        03-imagens          05-resultados
                                                               04-producao-video
                            ↑___________________________________________________________|
                                     os resultados realimentam as próximas pautas
```

1. **Pesquisa contínua** → todo dia a rotina automática gera um *briefing* com o que está quente, tendências políticas e temas sociais. → `00-inteligencia/`
2. **Banco de pautas** → as ideias que valem viram pauta qualificada (ângulo, formato, urgência). → `01-pautas/`
3. **Roteiro** → cada pauta aprovada vira um roteiro pronto de Reel ou carrossel, a partir dos templates. → `02-roteiros/`
4. **Produção** → busca de imagens (com direito de uso) e pipeline de edição de vídeo talking-head. → `03-imagens/`, `04-producao-video/`
5. **Resultados** → você registra o desempenho; a análise diz o que repetir e o que cortar, alimentando as próximas pautas. → `05-resultados/`

---

## Estrutura de pastas

| Pasta | O que guarda |
|---|---|
| `00-inteligencia/` | Briefings diários, tendências políticas e temas sociais monitorados |
| `01-pautas/` | Banco de pautas (backlog de ideias qualificadas) |
| `02-roteiros/` | Templates e roteiros prontos (Reels e carrosséis) |
| `03-imagens/` | Onde buscar imagens, regras de direito de uso, banco de referências |
| `04-producao-video/` | Pipeline de edição de vídeo talking-head |
| `05-resultados/` | Registro e análise de métricas e interações |
| `scripts/` | Utilidades (ex.: legendas automáticas, cortes) |

---

## Como me pedir cada coisa (comandos práticos)

Fale comigo em linguagem natural. Exemplos que o sistema entende:

- **"Roda o briefing de hoje"** → pesquiso e gero `00-inteligencia/briefings/AAAA-MM-DD.md`.
- **"Me dá 5 pautas sobre [tema]"** → qualifico e adiciono ao banco de pautas.
- **"Faz o roteiro do Reel da pauta X"** → gero o roteiro pronto a partir do template.
- **"Transforma a pauta Y em carrossel de 8 cards"** → gero o roteiro de carrossel.
- **"Acha imagens pra falar de [tema]"** → busco fontes com direito de uso e trago opções.
- **"Analisa os resultados dessa semana"** → leio `05-resultados/` e digo o que funcionou.

---

## Princípios editoriais (inegociáveis)

Conteúdo eleitoral exige responsabilidade. Este sistema sempre:

1. **Checa a fonte** antes de afirmar. Número de pesquisa sem instituto, data e margem de erro = não publica.
2. **Mostra os lados** nos conteúdos de análise/educação, mesmo quando há opinião.
3. **Separa fato de opinião** — quando for sua leitura, fica claro que é opinião.
4. **Não fabrica** falas, dados, imagens ou "pesquisas". Nada de desinformação.
5. **Respeita a legislação eleitoral** (TSE) — nada de conteúdo enganoso, deepfake de candidato ou desinformação sobre o processo de votação.
6. **Cita pesquisas corretamente**: instituto + data + margem de erro + registro no TSE.

---

## Rotina automática

Está configurada uma rotina diária que roda sozinha e entrega o briefing do dia.
Detalhes e como ligar/desligar/ajustar: **[`ROTINA-DIARIA.md`](ROTINA-DIARIA.md)**.
