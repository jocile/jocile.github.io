---
title: Documentação com Markdown
tags:
  - documentação
  - Markdown
description: Markdown é uma linguagem de marcação padrão para documentação
---
Markdown é uma linguagem de marcação leve com sintaxe de formatação de texto simples projetada para que ela possa ser convertida em HTML e muitos outros formatos usando uma ferramenta com o mesmo nome.  
Markdown é usado frequentemente para formatar arquivos readme, para escrever mensagens em fóruns de discussão on-line e para criar texto rico usando um editor de texto simples.

> [!Info]
> SIMPLESMENTE: É APENAS OUTRO TIPO DE ARQUIVO DE TEXTO, COMO .txt .doc .... (agora é .md) E COM UMA SINTAXE ESPECIAL.

## Porque usar Markdown

Porque é :

 * **FÁCIL** : A sintaxe é tão fácil que você pode aprender em um minuto ou dois, em seguida, escreva sem perceber nada estranho ou nerd.
 * **RÁPIDO** : Ele economiza tempo em comparação com outros tipos de arquivos / formatos de texto. Isso ajuda a aumentar a produtividade e os fluxos de trabalho do escritor.
 * **LIMPO** : Tanto a sintaxe como a saída são limpas, sem confusão com nossos olhos e simples de gerenciar.
 * **FLEXÍVEL** : Com apenas algumas configurações, o seu texto será traduzido atravessando qualquer plataforma lá fora, editável em qualquer software de edição de texto e conversível para uma ampla variedade de formatos.

**Em resumo**, os usuários comuns acharão útil em todos os casos, especialmente quando você precisar de algo melhor que o texto simples, mas menos funcional do que o Microsoft Word.  
**Para desenvolvedores**, Se você é preguiçoso para escrever código HTML, você vai adorar o markdown. **Além disso**, **Github** e muitos sites favorecem o markdown para o arquivo readme de projetos. Isso significa que você vai encontrar o markdown em sua vida de uma forma ou de outra.  

## Ferramentas para markdown

Conforme mencionado acima, qualquer editor pode ser usado para editar o markdown. No entanto, existem algumas ferramentas que podem ser úteis para você quando se trata de editar markdown.

 * **[*Stackedit*](https://stackedit.io)** 
 * **[*Dillinger*](http://dillinger.io/)**
 * **[*Typora*](https://www.typora.io/)** : Disponível para Mac e Windows, mínimo, livre de distração, vista ao vivo sem parecer, empacotada com muitas outras coisas como Imagens, Listas, Tabelas, Cercas de Código, Blocos de Matemática, YAML, Front Matters, Toc, ...
 * **[*Atom*](https://atom.io/)** : Editor de texto configurável, mais popular e versátil.
 * **[*Minimalist Markdown*](https://chrome.google.com/webstore/detail/minimalist-markdown-edito/pghodfjepegmciihfhdipmimghiakcjf?hl=en)** : Aplicativo do Google Chrome. Funciona em todos os lugares se você tiver o Chrome instalado (este é o meu favorito).
 * **[*Macdown*](http://macdown.uranusjr.com/)** : O Melhor para Mac.
 * **[*MarkdownPad*](http://markdownpad.com/)** : O Melhor para Windows.
 * **[*Remarkable*](https://remarkableapp.github.io/)** : O Melhor para Linux. 
 * **[*GITBOOK*](http://www.gitbook.com/)** : O GitBook é uma ferramenta de publicação moderna. Facilitando a escrita e a colaboração. Ambos suportam a Markdown e têm uma estreita relação com o amado Github.

## Sintaxe do Markdown  
Toda a sintaxe pode ser encontrada [aqui](https://daringfireball.net/projects/markdown/syntax) . Seria necessário muito esforço para descrever a sintaxe no texto (eles serão formatados), então, considere esta tabela abaixo para toda a sintaxe básica.  

| Formato        | Sintaxe      | Exemplo |
| ------|-----|-----|
| Itálico  	| \*Text\* 	| *Isto está em itálico* 	|
| Negrito  	| \*\*Bold\*\* 	| **Isto está em negrito** 	|
| Links inline 	| \[texto\](url aqui) 	| Um [link](http://www.github.com) 	|
| Imagens 	| \![Legenda\](url da img) 	| Uma imagem ![image](http://i.imgur.com/hRLuez2.png) 	|
| Link+imagens 	| \[\![Legenda\](url da img)\](url para a pagina)\] 	| Me clique [![me](http://i.imgur.com/hRLuez2.png)](https://www.youtube.com) 	|
| Notas de rodapé  	| Eu tenho mais \[^1\] pra dizer.   \[^1\]: diga aqui. 	| <a href="#section1">Ei, por favor leia as notas sobre essa tabela.  	|
| Quebras de linha 	| Double space + enter 	|  	|
| Listas não ordenadas 	| \* Item1     \*Item 2 	| <ul><li>item1</li><li>item2</li><li>item3</li><li>item4</li></ul> 	|
| Listas Ordenadas  	| 1. Item a    2. Item b 	| <ol><li>itema</li><li>itemb</li><li>itemc</li><li>itemd</li></ol>  	|
| Listas mistas 	| 1. Item 1      * item 1a 	|  <ol><li>itema</li></ol><ul><li> item1</li></ul>	|
| Citação 	| \> Texto citado 	|  <blockquote>Stay Hungry Stay Foolish</blockquote> 	|
| Preformatted 	| Comece cada linha com, dois espaços ou mais, faça o look do texto, e x a t a m e n t e, como, você, tipo i, s, t, o. 	|   Comece cada linha com, dois espaços ou mais, faça o look do texto, e x a t a m e n t e, como, você, tipo i, s, t, o. 	|
| Código 	| \`Insira o código\` 	| `cout<<"Hello world";` 	|
| Bloco de código/ Destaque de Sintaxe 	| \`\`\`Insira o código\`\`\` 	|  <a href="#section1">Ei, leia a nota abaixo desta tabela. 	|
| Títulos 	| `#`, `##`, `###`, `####`, `#####`, `######` (de h1 a h6) 	|  <h3>Isso é um título h3</h3>	|
| Riscado 	| \~~Insira o texto aqui\~~ 	| ~~Eu estou morto~~ 	|
| Tabelas 	| \| Tables   \|      Are      \|  Cool \| \|\----------\|\:\-------------\:\|------\:\| \| col 1 is\|  left-aligned \| $1600 \| | ![](http://i.imgur.com/EItt7mh.png) |

 Estas características dependem de cada versão de markdown.

> [!NOTA]
> O Markdown permite que você use escapes de barra invertida para gerar caracteres literais que de outra forma teria um significado especial na sintaxe de formatação da Markdown.

 `Assim? \ * Este \ * não é mais itálico, mas é cercado por asteriscos literais.`

 * Os vídeos do Youtube requerem algum trabalho adicional.
 
   Eles não podem ser adicionados diretamente, mas você pode adicionar uma imagem com um link para o vídeo como este:
 
  ```plaintext
  
  <a href="http://www.youtube.com/watch?feature=player_embedded&v=YOUTUBE_VIDEO_ID_HERE
  " target="_blank"><img src="http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg" 
  alt="Texto ALT da imagem aqui" width="240" height="180" border="10" /></a>
  ```
  
 * Markdown suporta Emoji 😆 😆 😘 😇 💚 ( obter alguns emojis [aqui](http://www.emoji-cheat-sheet.com/) )
 * Você pode usar a tag \<br/> para forçar uma quebra de linha. 
 * O espaço duplo, em seguida, se você quiser fazer uma nova linha se houver problemas para criar novas linhas.
 * Ver não é tão bom como praticar. Você pode criar um arquivo de markdown para você praticar ou fazê-lo online [aqui](http://www.markdowntutorial.com).
 *  As notas de rodapé e o destaque de sintaxe não fazem parte do Markdown original e são apenas suportados por certas versões de markdown (Feedback de [Sean Brody](https://goo.gl/ASZwEn))
 *  Qualquer URL (Como http://www.github.com/) será automaticamente convertido em um link clicável.  
 *  O suporte à tabela Markdown é projetado para lidar com a maioria das tabelas para a maioria das pessoas; não cobre todas as tabelas para todas as pessoas. Se você precisa de tabelas complexas, você precisará criá-las manualmente ou com uma ferramenta especificamente projetada para o formato de saída.  
 
## Referências

- [**Guia de Markdown no Gist**](https://gist.github.com/AlexandreQuintela/168e6fa0b6fc5c740c8658c9a5086914#file-markdown-md)
- [Criando documentação com Markdown no GitHub](https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github)
- [Exemplos de markdown](https://gist.github.com/ww9/44f08d44327a40d2ab309a349bebec57)
