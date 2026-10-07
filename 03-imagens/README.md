# 03 — Imagens

Onde buscar imagens para os conteúdos **com direito de uso** e como não cair em furada de copyright
(especialmente sério em conteúdo eleitoral).

## Bancos gratuitos com licença livre (uso comercial, sem atribuição obrigatória)
- **Unsplash** — unsplash.com
- **Pexels** — pexels.com (também vídeos/B-roll)
- **Pixabay** — pixabay.com
- **Openverse** — openverse.org (busca agregada; confira a licença de cada item)

## Imagens oficiais / institucionais (ótimas para conteúdo cívico)
- **Agência Brasil / EBC** — muitas sob Creative Commons (checar a licença na página da foto)
- **Fotos públicas de órgãos** (TSE, Câmara, Senado) — verificar termos de uso antes
- **Wikimedia Commons** — commons.wikimedia.org (cada arquivo tem a licença no rodapé)

## ⚠️ Regras de ouro (conteúdo eleitoral)
1. **Nunca** usar foto de candidato de banco pago/agência (Getty, AFP, Reuters) sem licença — risco real de multa.
2. **Nunca** gerar/alterar imagem de candidato de forma que pareça real (deepfake) — vedado pelo TSE.
3. Se usar imagem gerada por IA, **sinalizar que é ilustração/IA**.
4. Para rosto de pessoa comum, preferir banco livre (modelo já consentiu) a foto de internet.
5. Guardar o **link + licença** de cada imagem usada (prova de direito de uso).

## Banco de referências (registre o que já usou)
| Tema | Fonte | Link | Licença | Onde usei |
|---|---|---|---|---|
| Espectro esquerda/direita | Pixabay | https://pixabay.com/illustrations/search/left%20and%20right/ | Pixabay License (livre, uso comercial) | Carrossel "Esquerda e direita" |
| Balança / equilíbrio | Pixabay | https://pixabay.com/illustrations/search/balance%20scale/ | Pixabay License | Carrossel "Esquerda e direita" |
| Política (geral) | Pixabay | https://pixabay.com/illustrations/search/political%20art/ | Pixabay License | — |

## ⭐ Opção sem depender de banco: eu gero a arte

Como o proxy deste ambiente bloqueia APIs de imagem, a melhor saída (e muitas vezes a melhor arte)
é **eu gerar as imagens originais por código** — licença 100% sua, na identidade do seu feed, sem risco de copyright.

- **`scripts/gera_imagens_carrossel.py`** — renderiza um carrossel inteiro (1080×1350, 4:5) a partir de um
  roteiro: capa, cards de conteúdo, réguas e quadrante (espectro político), numeração e @ do perfil.
  Cores neutras (sem vermelho/azul partidário). Rode com:
  `python3 scripts/gera_imagens_carrossel.py`
  → saída em `03-imagens/gerado/<tema>/card-XX.png`.

Para ajustar cores/fonte à sua marca, edite o bloco "Identidade visual" no topo do script.
Exemplo já gerado: `03-imagens/gerado/esquerda-e-direita/`.

## Como pedir
- *"Gera as artes do carrossel X"* → eu adapto o gerador ao roteiro e entrego os PNGs prontos.
- *"Acha imagens pra falar de [tema]"* → eu trago opções de bancos livres (links + licença), via busca web.
