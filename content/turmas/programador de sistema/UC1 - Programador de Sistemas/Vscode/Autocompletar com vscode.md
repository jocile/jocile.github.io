---
title: "Autocompletar com vscode"
date: 2026-09-22
draft: false
tags:
  - editando-codigo
  - vscode
description: "Pequenos trechos de código pré-definidos que podem ser inseridos rapidamente para automação e economia de tempo."
---

**Snippets** são pequenos trechos de código pré-definidos que podem ser inseridos rapidamente em seu editor de texto. Eles são uma forma de automação que economiza tempo e ajuda a evitar erros comuns. Na [[IDE VScode]], você pode criar e usar seus próprios snippets personalizados para agilizar o desenvolvimento. Vou explicar como fazer isso:

1. Abra o **VS Code**.
2. Pressione **Ctrl+Shift+P** (ou **Cmd+Shift+P** no macOS) para abrir a paleta de comandos.
3. Digite "**Configure User Snippets**" e selecione a opção correspondente para abrir o gerenciador de snippets.

Aqui estão os passos detalhados:

1. **Abrir o Gerenciador de Snippets**:
   - Pressione **Ctrl+Shift+P** (ou **Cmd+Shift+P** no macOS).
   - Digite "**Configure User Snippets**" e selecione a opção correspondente.
   - Escolha a linguagem na qual deseja criar o snippet personalizado ou selecione "**Global snippets**" para criar um snippet que funcione em qualquer linguagem.

2. **Criar um Snippet Personalizado**:
   - Após selecionar a linguagem, informe um nome para o arquivo do seu snippet.
   - O arquivo será aberto com um exemplo de snippet vazio.
   - Defina o corpo do snippet com o código que deseja inserir quando o snippet for ativado.
   - Use placeholders como **$1**, **$2**, etc., para indicar onde o cursor será posicionado após a inserção do snippet.

3. **Exemplo de Snippet**:
   - Aqui está um exemplo simples de um snippet chamado "**Print to Console**":

     ```json
     {
         "Print to Console": {
             "prefix": "log",
             "body": [
                 "console.log('$1');",
                 "$2"
             ],
             "description": "Prints a message to the console"
         }
     }
     ```

     Neste exemplo, o snippet é acionado pelo prefixo "**log**". Quando ativado, ele insere `console.log()` e posiciona o cursor nos lugares indicados pelos placeholders.

4. **Salvar o Arquivo**:
   
Salve o arquivo e seu novo snippet personalizado, na pasta `.vscode`, que estará pronto para ser usado:

  `.vscode\nome-do-arquivo.code-snippets`

Agora você pode criar seus próprios snippets para agilizar o desenvolvimento no VS Code! 🚀¹²³.

## Referências

- (1) Aprenda a criar seus snippets no VSCode facilmente - Cubos Academy. https://blog.cubos.academy/programacao-snippets-no-vscode/.
- (2) Como criar seus próprios snippets no Visual Studio Code. https://imasters.com.br/desenvolvimento/como-criar-seus-proprios-snippets-no-visual-studio-code.
- (3) Snippets in Visual Studio Code. https://code.visualstudio.com/docs/editor/userdefinedsnippets.
- (4) Code Snippets no Visual Studio Code | by Joel Rodrigues | Medium. https://medium.com/@joelrodrigues/code-snippets-no-visual-studio-code-1acb15cbb58e.

[Meu snipet no Gist](https://gist.github.com/jocile/18d4db8ad7dc4631742dd09722d1b162)
