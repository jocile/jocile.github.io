---
title: Markdown
description: é uma linguagem de marcação leve com sintaxe de formatação de texto simples
date: '2026-08-12'
draft: false
tags:
- Markdown
---

## Editor

<https://pandao.github.io/editor.md/en.html>

Markdown é um estilo de texto na web. Você controla a exibição do documento; formando palavras como **negrito** ou _itálico_ adicionar imagens e cria listas, etc.

## Títulos

```
## Subtítulo nível 2
### Subtítulo nível 3
```

## Formatação

```
_Italico_
**Negrito**
**_Italico e negrito_**
```

```
Links: [Texto do link](https://jocile.com/)
```

```
 Listas:
- Item 1
- Item 2
- Item 3
```

## Imagens

```
 Imagens:
Inline-style: 
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

Reference-style: 
![alt text][logo]

```

## Código


`Código` em linha tem `áspas ao redor`.


````
Blocos de código são envoltas por linhas com três áspas ```, 
ou são identadas com quatro espaços.
````

## Tabelas

```

| Tabelas            | são                     | legais |
| -----------------  |:-----------------------:| ------:|
| col 3 é            | alinhada para à direita |  $1600 |
| col 2 is           | centralizada            |    $12 |
| listras das zebras | são legais              |     $1 |

Devem haver ao menos 3 hifens ('-') separando cada célula do cabeçalho.
As barras externas (`|`) são opcionais e você não precisa fazer as células em Markdown estarem bem alinhadas.

Markdown | menos | bonito
--- | --- | ---
*ainda* | `renderiza` | **bem**
1 | 2 | 3

```

| Tabelas            | são                     | legais |
| -----------------  |:-----------------------:| ------:|
| col 3 é            | alinhada para à direita |  $1600 |
| col 2 is           | centralizada            |    $12 |
| listras das zebras | são legais              |     $1 |

---

Markdown | menos | bonito
--- | --- | ---
_ainda_ | `renderiza` | **bem**
1 | 2 | 3

---

## Citações

```
> Citações são muito úteis em em email para emular respostas textuais.
> Esta linha faz parte da mesma citação.
```

> Citações são muito úteis em Um email para emular respostas textuais.
> Esta linha faz parte da mesma citação.

Underscores

<https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet>

## Links no final do arquivo

```
Link normal [Join the Google Group](http://groups.google.com/group/celluloid-ruby)

Link que seria repetido [Join the Google Group][google-group]

Links organizados no final do arquivo:

[google-group]: http://groups.google.com/group/celluloid-ruby
```

## Selos

- Para adicionar selos, que são componentes descritivos, ao README.md

[Shields](https://shields.io/)

## Referências

- [Sintaxe básica de escrita e formatação - Documentos do GitHub](https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [[documentacao-com-Markdown]]
- [Referência da syntaxe markdown na UFRGS](http://www.if.ufrgs.br/fis01069/sintaxemarkdown.html)
- [Referência da syntaxe markdown no firebal](https://daringfireball.net/projects/markdown/syntax)
- [Referência da syntaxe markdown no GitHub](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf)
- <https://digitalinnovation.one/artigos/tutorial-criando-um-readme-bonitao-para-o-seu-github>
