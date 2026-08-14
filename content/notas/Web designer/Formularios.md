---
title: Formulários HTML
description: possui campos para coletar informações dos usuários
date: '2026-08-12'
draft: false
tags:
- html
- Webdesign 
---

## Curso de HTML e Desenvolvimento Web 

### Introdução aos Formulários 

Este artigo descreve sobre formulários dentro do HTML, que são essenciais para interagir com os usuários na web. veremos os conceitos básicos de como criar e utilizar formulários em sites. 

---

### O que é um Formulário? 

Um formulário no HTML nada mais é do que um trecho da sua página onde você coloca campos para coletar informações dos usuários. Esses dados são enviados para um servidor quando o usuário clica em um botão de envio. 

É importante mencionar que todo site moderno trabalha com essa ideia: formulários no lado do cliente (navegador) e servidores no backend, responsáveis por processar as informações. Isso também é conhecido como comunicação client-server. 

---

### A Tag form 

Agora vamos ao básico: a tag `<form>` é o elemento que define um formulário em HTML5. Ela abre e fecha, e dentro dela você coloca os campos de entrada (inputs). 

Vamos dar uma olhada no código abaixo como exemplo: 

```html 
<form> 
 <!-- Campos aqui --> 
</form> 
``` 

Essa tag é bem simples na teoria, mas quando combinada com JavaScript e outros atributos, se torna poderosa. Nas próximas aulas vamos explorar isso mais profundamente! 

---

#### O Elemento `fieldset`

O elemento `<fieldset>` agrupa controles de formulário relacionados. Ele atua como um container para outros elementos de formulário, como legendas inputs, selects, etc., estabelecendo seções lógicas dentro do seu formulário. Por exemplo:

```html
<fieldset>
 <legend>Informações Pessoais</legend>
 
 <!-- Outros elementos input e select aqui -->
</fieldset>

<fieldset>
 <legend>Dados de Contato</legend>
 
 <!-- Outros elementos input e select aqui -->
</fieldset>
```

Essa agrupação ajuda os usuários a compreenderem a relação entre os controles do formulário. Ela também auxilia leitores de tela na navegação mais eficiente pelos formulários.

O uso do `<fieldset>` com legendas elementos `legend` melhora significativamente a navegação dos leitores de tela. Por exemplo:

```html
<fieldset>
 <legend>Esta é uma seção bem estruturada</legend>
 
 <!-- Controles do formulário -->
</fieldset>

<fieldset aria-labelledby="section-label">
 <label id="section-label">Esta é outra forma de rotular um fieldset</label>
 
 <!-- Controles do formulário -->
</fieldset>
```

### Campos de Entrada (Inputs) 

Os campos são os elementos que você usa para coletar dados do usuário. Existem vários tipos de inputs: 

#### Input Text 

É o campo padrão para entrada de texto, como nome ou e-mail. 

```html 
<input type="text" name="nome"> 
```

#### Input Number 

Aceita apenas números e é útil para campos numéricos, como idade ou preço.

```html 
<input type="number" name="idade"> 
```

#### Input Password 

Esconde os caracteres digitados, ideal para senhas sensíveis.

```html
<input type="password" name="senha">
```

---

#### O Atributo `placeholder`

O atributo `placeholder` fornece uma dica ou exemplo sobre o que deve ser inserido no elemento `<input>` quando nenhum valor ainda foi fornecido. Por exemplo:

```html
<input type="text" placeholder="Digite seu nome completo">
```

Quando o usuário foca neste campo de entrada, o `placeholder` desaparece para dar espaço ao texto dele. Embora úteis para orientar os usuários, placeholders não devem substituir completamente os rótulos.

#### O Elemento `<option>`

O elemento `<option>` define uma única escolha dentro do menu dropdown `<select>`. Por exemplo:

```html
<select>
 <option value="">Selecione seu país</option>
 <option value="usa">Estados Unidos</option>
 <option value="canada">Canadá</option>
 <!-- Mais opções aqui -->
</select>
```

Cada opção oferece uma escolha selecionável da lista de opções disponíveis. É possível desabilitar as opções (ainda visíveis, mas não selecionáveis) ou defini-las como selecionadas por padrão.

#### O Atributo `required`

O atributo `required` torna um controle de formulário obrigatório antes de submeter os dados. Por exemplo:

```html
<input type="text" required placeholder="Digite seu nome">
```

Isso garante que os usuários não possam enviar o formulário sem fornecer seu nome. É especialmente útil para campos como e-mail, senha ou outros pontos de informação crítica.

### Aplicações Práticas

Considere como combinar esses atributos em um cenário real:

```html
<form>
 <fieldset>
 <legend>Criação de Conta</legend>
 
 <label for="username">Usuário:</label>
 <input type="text" id="username" required placeholder="Escolha seu nome de usuário">
 
 <br>
 
 <label for="email">E-mail:</label>
 <input type="email" id="email" required placeholder="seu@email.com">
 </fieldset>

 <br>

 <fieldset>
 <legend>Preferências de Contato</legend>
 
 <!-- Mais elementos do formulário aqui -->
 </fieldset>

 <button type="submit">Enviar Formulário</button>
</form>
```

Neste exemplo, os campos de usuário e e-mail são obrigatórios. O usuário não pode enviar o formulário sem completar esses campos. Os placeholders orientam sobre a formatação adequada para cada campo.

---

### Enviando Dados: Atributos Name e Action 

Quando falamos de um formulário, é fundamental entender dois atributos: `name` e `action`. 

#### O atributo name 

Ele define como os dados serão identificados no servidor. É como se fosse o nome da variável que vai receber a informação.

```html
<input type="text" name="usuario">
```

#### O atributo action 

Indica para onde os dados devem ser enviados quando o formulário for submetido.

```html
<form action="/processar-dados.html">
 <!-- Campos aqui -->
</form>
```

---

### Método POST vs GET 

Outro aspecto importante é o método de envio dos dados. Existem dois métodos comuns: `POST` e `GET`. 

#### Método POST 

Envia os dados no corpo da requisição (body) e não aparece na URL. É mais seguro, ideal para informações sensíveis.

```html
<form method="post">
 <!-- Campos aqui -->
</form>
```

#### Método GET 

Envia os dados pela URL e é visível para qualquer pessoa que acessar o link do formulário. Não recomendado para senhas ou dados confidenciais.

---

### Target: Abrir em Nova Aba 

O atributo `target` controla como a página de destino é aberta quando um formulário é enviado. Por padrão, ele abre na mesma aba (`_self`). Se você quiser abrir em uma nova aba, pode usar `_blank`.

```html
<form target="_blank">
 <!-- Campos aqui -->
</form>
```

---

### Autocomplete: Desativando o Completamento 

Para evitar que o navegador preencha automaticamente os campos (como no caso de um formulário de login), use `autocomplete="off"`.

```html
<input type="text" autocomplete="off">
```

---

### JavaScript e Eventos do Formulário

Quando você envia um formulário, é possível adicionar eventos para controlar o que acontece antes. O evento `onsubmit` pode ser usado para validar os dados ou executar outras ações.

```html
<form onsubmit="validarFormulario(event)"> 
 <!-- Campos aqui --> 
</form> 

<script> 
function validarFormulario(event) { 
 // Lógica de validação aqui 
} 
</script>
```

---

### Conclusão

Entenderemos que formulários são a ponte entre o usuário e o servidor. Eles permitem coletar dados, realizar cadastros e muito mais! 

Na próxima aula, vamos falar sobre os diferentes tipos de inputs em detalhes — text, number, password, checkbox, radio button, select, etc. 

### Referências

- [HTML Forms](https://www.w3schools.com/html/html_forms.asp)
- [Exemplo de formulário de cadastro de alunos no GitHub]([https://github.com/jocile/controle-academico/blob/main/cadastro-de-alunos.html](https://jocile.github.io/controle-academico/cadastro-de-alunos.html))
- [[Web Designer Senac]]
