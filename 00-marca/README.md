# 00 — Marca (fonte única da verdade)

Tudo que define **quem você é** como creator mora aqui. Toda sessão do Claude (esta, local, cloud, futura)
e todos os scripts leem desta pasta. É isso que te tira da dependência de um chat ou de um Projeto específico.

| Arquivo | O que guarda | Status |
|---|---|---|
| `marca.json` | Identidade visual em dados (cores, fontes, @perfil) que os scripts consomem | ⚙️ defaults — troque pelos seus |
| `tom-de-voz.md` | Como você fala: princípios, o que evita, exemplos | ✍️ destilado das suas skills — complete com o do Projeto |
| `identidade-visual.md` | Cores, fontes, logo, estilo de template | 🟡 placeholders — preencha com o manual |
| `pilares-e-posicionamento.md` | Sobre o que você fala, pra quem, qual seu lugar | 🟡 placeholder |

## Como isso alimenta o sistema
- Os **roteiros** (`02-roteiros/`) seguem o `tom-de-voz.md`.
- As **artes** (`scripts/gera_imagens_carrossel.py`) leem cores/fontes/@ do `marca.json`.
- As **pautas** e análises respeitam seus `pilares-e-posicionamento.md`.

## Como trazer o conteúdo do seu Projeto do Claude
O conhecimento de um Projeto do claude.ai **não chega sozinho** numa sessão de código (fica isolado no Projeto).
Para trazer, faça uma vez:
1. Abra o Projeto, copie o texto dos docs (tom de voz, manual de identidade) **ou** anexe os arquivos aqui no chat.
2. Me diga "atualiza a pasta 00-marca com isso" — eu estruturo tudo nos arquivos acima.
3. Se houver cores/fontes, eu atualizo o `marca.json` e **todas as artes passam a sair na sua marca**.

> Alternativa: se esses mesmos arquivos estiverem no **Google Drive**, eu tenho o conector nesta sessão e
> posso ler direto — é só você mandar o link ou o nome da pasta.
