---
title: "Gestão de Produtos 3: visualização do ranking de vendas"
date: 2026-10-27
draft: false
tags:
  - python/bd
  - pandas
  - seaborn
  - visualizacao-de-dados
description: "Gere um gráfico de barras horizontal do ranking de vendas com Seaborn e Matplotlib, salve o arquivo PNG e prepare os arquivos para a aplicação web."
---

Um ranking em tabela mostra os números. Um gráfico bem construído mostra a **conclusão**. Nesta atividade você transforma o ranking de vendas em um gráfico de barras horizontal e **salva a imagem em arquivo**, pois ela será usada na página web da próxima nota.

> [!info] Ficha da atividade
>
> - **Ambiente:** Google Colab
> - **Tempo estimado:** 30 minutos
> - **Pré-requisito:** [[produtos-02-vendas-estoque|Nota 2]] concluída (tabela `Vendas` preenchida)
> - **Resultado esperado:** o arquivo `static/ranking_vendas.png` gerado e baixado, junto com o `gestao_produtos.db`
> - **Próxima nota:** [[produtos-04-api-bottle|API e relatório com Bottle]]

## Por que barras horizontais?

Gráficos de barras horizontais são ideais para rankings: os nomes dos produtos ficam legíveis, sem rotação, e a comparação entre quantidades é imediata.

## Passo 1: carregar os dados

Como o Colab pode ter sido reiniciado, carregue o ranking novamente a partir do banco.

```python
import sqlite3
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

conn = sqlite3.connect("gestao_produtos.db")

df_vendas = pd.read_sql_query("""
SELECT
    p.nome AS Produto,
    c.nome_categoria AS Categoria,
    SUM(v.quantidade) AS Qtd_Vendida,
    SUM(v.quantidade * p.preco) AS Faturamento_Total
FROM Produto p
LEFT JOIN Vendas v ON p.id_produto = v.id_produto
LEFT JOIN Categoria c ON p.id_categoria = c.id_categoria
GROUP BY p.id_produto, p.nome, c.nome_categoria
ORDER BY Qtd_Vendida DESC;
""", conn)
conn.close()

df_vendas["Qtd_Vendida"] = df_vendas["Qtd_Vendida"].fillna(0).astype(int)
df_vendas["Faturamento_Total"] = df_vendas["Faturamento_Total"].fillna(0.0)

df_vendas
```

## Passo 2: desenhar e salvar o gráfico

O título é montado a partir dos dados, então continua correto se os números mudarem. A primeira barra recebe uma cor de destaque, e as demais ficam em tom neutro.

```python
sns.set_theme(style="whitegrid")

# Cores: destaque para o líder, tom neutro para os demais
DESTAQUE, NEUTRA = "#1f4e79", "#9ab7d3"
paleta = {
    produto: (DESTAQUE if i == 0 else NEUTRA)
    for i, produto in enumerate(df_vendas["Produto"])
}

fig, ax = plt.subplots(figsize=(10, 5))

sns.barplot(
    data=df_vendas,
    x="Qtd_Vendida",
    y="Produto",
    hue="Produto",
    palette=paleta,
    legend=False,
    ax=ax,
)

lider = df_vendas.iloc[0]
ax.set_title(
    f"{lider['Produto']} lidera em volume com {lider['Qtd_Vendida']} unidades vendidas",
    fontsize=13, fontweight="bold", pad=15,
)
ax.set_xlabel("Quantidade de unidades vendidas", fontsize=11)
ax.set_ylabel("")

# Rótulo numérico ao lado de cada barra
for barra in ax.patches:
    largura = barra.get_width()
    if largura > 0:
        ax.annotate(
            f"{int(largura)} un.",
            (largura, barra.get_y() + barra.get_height() / 2),
            ha="left", va="center",
            xytext=(6, 0), textcoords="offset points",
            fontsize=10, fontweight="bold",
        )

sns.despine(top=True, right=True)
plt.tight_layout(pad=1.5)

# Salve ANTES de plt.show(), que pode limpar a figura
Path("static").mkdir(exist_ok=True)
plt.savefig("static/ranking_vendas.png", dpi=150, bbox_inches="tight")
plt.show()
```

> [!warning] Salve antes de exibir
> Se `plt.savefig()` vier depois de `plt.show()`, o arquivo pode sair em branco. Mantenha a ordem do código acima.

Confirme que o arquivo existe:

```python
!ls -l static
```

## Passo 3: baixar os arquivos para o computador

A Nota 4 roda no seu computador, então traga o gráfico e o banco do Colab.

```python
from google.colab import files

files.download("static/ranking_vendas.png")
files.download("gestao_produtos.db")
```

> [!note] Guarde os dois arquivos
> Você vai colocar `ranking_vendas.png` na pasta `static/` e `gestao_produtos.db` na raiz do projeto da próxima nota.

## Como ler o gráfico

1. **Leitura direta:** a Camisa Polo lidera com 10 unidades, seguida pelo Smartphone (7) e pela Cadeira de Escritório (5).
2. **Destaque único:** apenas a barra do líder tem cor forte, o que conduz o olhar para a conclusão.
3. **Rótulos nas barras:** o valor exato aparece ao lado de cada barra, dispensando a leitura aproximada pelo eixo.
4. **Eixo começando em zero:** em gráficos de barras, o comprimento representa o valor. Cortar o eixo exagera as diferenças.

## Desafios

> [!question] Desafio 1: gráfico de faturamento
> Crie um segundo gráfico com o **faturamento por produto** e salve como `static/ranking_faturamento.png`. O líder é o mesmo do gráfico de unidades? O que isso ensina sobre escolher a métrica certa?

> [!success]- Solução do desafio 1
>
> ```python
> df_fat = df_vendas.sort_values("Faturamento_Total", ascending=False)
>
> fig, ax = plt.subplots(figsize=(10, 5))
> sns.barplot(data=df_fat, x="Faturamento_Total", y="Produto", color="#1f4e79", ax=ax)
>
> lider_fat = df_fat.iloc[0]
> ax.set_title(f"{lider_fat['Produto']} lidera em faturamento", fontsize=13, fontweight="bold")
> ax.set_xlabel("Faturamento (R$)")
> ax.set_ylabel("")
> sns.despine(top=True, right=True)
> plt.tight_layout()
>
> plt.savefig("static/ranking_faturamento.png", dpi=150, bbox_inches="tight")
> plt.show()
> ```
>
> O líder em faturamento é o **Smartphone** (R$ 11.200,00), enquanto o líder em unidades é a Camisa Polo. Um produto barato vende muito, mas um produto caro pode render mais. A métrica escolhida muda a conclusão.

> [!question] Desafio 2: faturamento por categoria
> Agrupe `df_vendas` por `Categoria`, some o faturamento e gere um gráfico de barras. Qual categoria lidera?

> [!tip]- Dica
> Use `df_vendas.groupby("Categoria")["Faturamento_Total"].sum().sort_values(ascending=False)` e passe o resultado para `sns.barplot`. A categoria líder é **Eletrônicos**, com R$ 18.200,00.

## Erros comuns

| Sintoma | Causa provável | Como corrigir |
| --- | --- | --- |
| Imagem salva em branco | `savefig` chamado depois de `show` | Chame `savefig` antes de `show` |
| `no such table: Vendas` | Banco do Colab sem a Nota 2 | Refaça a Nota 2 ou use o script de restauração |
| `FileNotFoundError` no `savefig` | Pasta `static` não existe | Execute `Path("static").mkdir(exist_ok=True)` |
| `files.download` não abre nada | Navegador bloqueou o download | Autorize downloads para o Colab ou baixe pelo painel de arquivos à esquerda |

## Checklist de verificação

- [ ] O `DataFrame` mostra 5 produtos, com a Camisa Polo no topo
- [ ] O título do gráfico cita o produto líder e a quantidade
- [ ] Apenas a barra do líder está em destaque
- [ ] O arquivo `static/ranking_vendas.png` existe e abre corretamente
- [ ] Os arquivos `ranking_vendas.png` e `gestao_produtos.db` foram baixados

## Próximo passo

Continue em [[produtos-04-api-bottle|API e relatório com Bottle]]. A partir dela, o trabalho é feito no seu computador.
