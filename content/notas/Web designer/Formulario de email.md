---
title: Formulário de email
description: O formulário de contato que manda email
date: '2026-08-12'
draft: false
tags:
- html
- Webdesign 
---

# Habilitar Formulário de Contato com Web3Forms

O formulário de contato em `index.html` atualmente possui `action="#"` e não envia mensagens. O objetivo é integrá-lo com o **[Web3Forms](https://app.web3forms.com/)** para que os e-mails sejam recebidos diretamente na sua caixa sem precisar de servidor.

```html
<form method="post" action="#">
<div class="row">
	<div class="col-6 col-12-small">
		<input type="text" name="name" id="name" placeholder="Nome" />
	</div>
	<div class="col-6 col-12-small">
		<input type="text" name="email" id="email" placeholder="Email" />
	</div>
	<div class="col-12">
		<input type="text" name="subject" id="subject" placeholder="Assunto" />
	</div>
	<div class="col-12">
		<textarea name="message" id="message" placeholder="Mensagem"></textarea>
	</div>
	<div class="col-12">
		<ul class="actions">
			<li><input type="submit" value="Enviar" /></li>
			<li><input type="reset" value="Limpar" class="alt" /></li>
		</ul>
	</div>
</div>
</form>
```

## Serviço web3forms

> [!IMPORTANT]
> **Você precisará criar uma conta gratuita no Web3Forms para obter sua chave de acesso (access key).**
> 1. Acesse [https://web3forms.com](https://web3forms.com)
> 2. Digite seu e-mail e clique em **"Create your Access Key"**
> 3. Verifique sua caixa de entrada e copie a **access key** enviada por e-mail
> 4. Substitua o placeholder `SUA_ACCESS_KEY_AQUI` no HTML após a implementação

> [!NOTE]
> O Web3Forms não exige cadastro com senha — apenas um e-mail e a chave de acesso.

---

## Mudanças propostas

### Formulário de Contato

- Alterar o `action` do form para o endpoint do Web3Forms: `https://api.web3forms.com/submit`
- Alterar `method` para `post`
- Adicionar `<input type="hidden" name="access_key" value="SUA_ACCESS_KEY_AQUI" />`
- Adicionar campo `subject` como hidden para personalizar o assunto do e-mail recebido
- Corrigir o campo de e-mail: mudar `type="text"` para `type="email"` (validação nativa do browser)
- Adicionar campo `botcheck` oculto (honeypot anti-spam exigido pelo Web3Forms)
- Adicionar `id="contact-form"` no `<form>` para poder capturar a resposta via JavaScript
- Adicionar `<div id="result">` para exibir mensagem de sucesso/erro ao usuário

O Formulário ficou assim:

```html
<form id="contact-form" method="post" action="https://api.web3forms.com/submit">
<!-- Web3Forms -->
<input type="hidden" name="access_key" value="SUA_ACCESS_KEY_AQUI" />
<input type="hidden" name="subject" value="Nova mensagem do site - Jocilé" />
<input type="checkbox" name="botcheck" id="botcheck" style="display:none;" />
<div class="row">
	<div class="col-6 col-12-small">
		<input type="text" name="name" id="name" placeholder="Nome" required />
	</div>
	<div class="col-6 col-12-small">
		<input type="email" name="email" id="email" placeholder="Email" required />
	</div>
	<div class="col-12">
		<input type="text" name="subject_field" id="subject_field" placeholder="Assunto" />
	</div>
	<div class="col-12">
		<textarea name="message" id="message" placeholder="Mensagem" required></textarea>
	</div>
	<div class="col-12">
		<div id="form-result" style="display:none; margin-bottom:1em; padding:1em; border-radius:4px;"></div>
		<ul class="actions">
			<li><input type="submit" id="submit-btn" value="Enviar" /></li>
			<li><input type="reset" value="Limpar" class="alt" /></li>
		</ul>
	</div>
</div>
</form>
```

### JavaScript de Feedback

- Adicionar script inline que intercepta o `submit` do formulário via `fetch` (AJAX), exibe mensagem de sucesso/erro sem recarregar a página, e limpa o formulário após envio bem-sucedido.

```js
<!-- Formulário de Contato - Web3Forms -->
<script>
	document.getElementById('contact-form').addEventListener('submit', function(e) {
		e.preventDefault();

		var submitBtn = document.getElementById('submit-btn');
		var resultDiv = document.getElementById('form-result');

		submitBtn.value = 'Enviando...';
		submitBtn.disabled = true;
		resultDiv.style.display = 'none';

		var formData = new FormData(this);

		fetch('https://api.web3forms.com/submit', {
			method: 'POST',
			body: formData
		})
		.then(function(response) { return response.json(); })
		.then(function(data) {
			resultDiv.style.display = 'block';
			if (data.success) {
				resultDiv.style.background = '#2d6a4f';
				resultDiv.style.color = '#d8f3dc';
				resultDiv.innerHTML = '&#10003; Mensagem enviada com sucesso! Em breve entrarei em contato.';
				document.getElementById('contact-form').reset();
			} else {
				resultDiv.style.background = '#7b2d00';
				resultDiv.style.color = '#ffd6c0';
				resultDiv.innerHTML = '&#10007; Ocorreu um erro ao enviar. Por favor, tente novamente.';
			}
			submitBtn.value = 'Enviar';
			submitBtn.disabled = false;
		})
		.catch(function() {
			resultDiv.style.display = 'block';
			resultDiv.style.background = '#7b2d00';
			resultDiv.style.color = '#ffd6c0';
			resultDiv.innerHTML = '&#10007; Erro de conexão. Verifique sua internet e tente novamente.';
			submitBtn.value = 'Enviar';
			submitBtn.disabled = false;
		});
	});
</script>
```

---

## Plano de Verificação

1. Após criar a access key no Web3Forms, substituir o placeholder no HTML
2. Abrir `index.html` no browser, preencher o formulário e clicar em **Enviar**
3. Verificar se a mensagem de confirmação aparece na tela
4. Verificar se o e-mail chegou na caixa cadastrada no Web3Forms
