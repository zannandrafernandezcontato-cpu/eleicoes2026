# ⏰ Rotina automática diária

Uma rotina agendada roda **sozinha toda manhã** (horário de Brasília), pesquisa o cenário
e entrega o briefing do dia — sem você precisar pedir.

## O que ela faz a cada manhã
1. Atualiza o repositório (pega a última versão da branch).
2. Pesquisa na web: fato do dia, tendências políticas e temas sociais ligados às eleições 2026.
3. Gera `00-inteligencia/briefings/AAAA-MM-DD.md` com: o que está quente, tendências, temas sociais e **5 pautas sugeridas**.
4. Adiciona as pautas novas em `01-pautas/banco-de-pautas.md` (seção *A avaliar*).
5. Atualiza `tendencias.md` e `temas-sociais.md` se algo mudou.
6. Faz commit e push na branch do projeto.
7. Respeita os **princípios editoriais** do `README.md` (checar fonte, mostrar os lados, nada de desinformação).

Quando acordar, é só abrir o briefing do dia e escolher o que produzir.

## Horário
Configurada para rodar **toda manhã (~06:50, horário de Brasília)**.
Quer outro horário, ou só em dias específicos? Me diga que eu ajusto.

## Ligar / desligar / ajustar
- **Pausar:** "pausa a rotina diária".
- **Mudar horário:** "roda a rotina às 7h30".
- **Rodar agora:** "roda o briefing de hoje".
- **Retomar:** "religa a rotina diária".

> A rotina abre uma sessão nova a cada manhã (não depende desta janela ficar aberta).
> O resultado chega pronto no repositório.
