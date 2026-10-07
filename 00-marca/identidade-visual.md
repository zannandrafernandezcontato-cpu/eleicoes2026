# 🎨 Identidade visual — dossiê @zannandra

> Valores em dados: [`marca.json`](marca.json). Detalhe e racional: [`guia-identidade-estrategia.md`](guia-identidade-estrategia.md) §5.

## Princípio reitor
**Um sistema visual por peça** — cada uma com cara própria, sem repetir o layout anterior.
Consistência vem do **chassi** (paleta + tipografia + método); variação vem do **acento de cada peça**.
**Sobriedade persuade:** referência é **data-viz sóbrio de dossiê**, não viral.

## Paleta oficial (registrada 07/10/2026)
**Núcleo:** Marrom tinta `#53382F` · Verde `#4D774E` · Amarelo âmbar `#F2B134` · Areia `#EBCCA2` (fundo principal) · Papel `#F2E4CC` (fundo dossiê)
**Apoio:** Verde escuro `#3C5E3D` · Papel alt `#F6E3C8` (PCD/C5) · Bege neutro `#D8C3A1` · Trilho de barra `#E7D4B5`

## Guardrail verde-amarelo (regra #7)
O **verde-amarelo saturado da bandeira** entra **só no card de fechamento que nomeia o Lula**.
O verde-oliva e o âmbar **dessaturados** do dossiê correm na série toda. Mesmo liberado, **o sóbrio convence mais**.

## Tipografia
- Títulos/corpo: **Archivo** (500/700/900)
- Dados/rótulos/rodapé: **IBM Plex Mono**
> As fontes não estão instaladas neste ambiente — os scripts usam DejaVu como fallback. Para render fiel,
> colocar os `.ttf` em `00-marca/fontes/` e apontar no `marca.json`.

## Regras de aplicação
Fonte no próprio card em toda afirmação · datar sempre (sem tempo relativo) · sem hashtag de campanha ·
data-viz com **eixo no zero** + fonte no gráfico · card de fechamento blindado.

## Catálogo já usado (não repetir layout)
C1 três chaves · C2 planos frente a frente · C3 mapa+carimbos · C4 bolha WhatsApp+nota fiscal ·
C5 comprimidos cuidar/direito · C6 data-viz de dossiê · C7 mapa do poder · Agro nota fiscal rural.

## ⚠️ Decisões em aberto (do próprio guia)
1. **Dois fundos claros** circulando (`#EBCCA2` areia e `#F2E4CC` papel) — escolher um padrão?
2. **Tipografia divergente:** §5.5 diz Archivo + IBM Plex Mono; §6.3 (vídeo) cita Bricolage Grotesque + IBM Plex Sans. Padronizar.
3. **Regra #7 × paleta:** a paleta oficial tem verde e amarelo; a regra, lida ao pé da letra, restringe. O guia já resolve (mira o par *saturado* da bandeira), mas vale decisão explícita + fixar os hex do verde-amarelo do fecho.

## Sobre as artes geradas por código (importante)
Seu sistema visual é **bespoke por peça**, feito no **canvas do Claude Design**. O gerador
`scripts/gera_imagens_carrossel.py` é um **rascunho/scaffold** que respeita a paleta — **não é** o seu
design system. Serve para prototipar rápido; a arte final da série sai do seu fluxo de design.
