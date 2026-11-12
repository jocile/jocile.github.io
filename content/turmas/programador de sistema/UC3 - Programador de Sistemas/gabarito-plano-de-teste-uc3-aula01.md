---
title: Gabarito - Plano de teste da Aula 1 da UC3
description: Gabarito do docs/plano-de-teste.md da uc3.01, com notas de correção. Não publicar.
date: 2026-11-11
draft: false
tags:
  - programador-sistemas/gabarito
  - uc3
---

%%
# Plano de teste: Sistema Gestão de Produtos

> [!warning] Uso exclusivo do docente
> Não publicar no Quartz. Este gabarito supõe o repositório-base em **versão correta**, ou seja, sem os defeitos da v0.9 (que só entram na Aula 4). Por isso os 6 casos devem sair **Aprovados**. Um caso Reprovado na Aula 1 indica problema no repositório-base ou erro de execução do aluno.

---
%%

## 1. Identificação

- **Sistema:** Gestão de Produtos (Loja do Bairro, caso fictício)
- **Versão testada:** repositório-base entregue na Aula 1
- **Responsáveis:** (nomes da dupla)
- **Data:** 11/11/2026

## 2. Objetivo

Verificar, antes da entrega à Loja do Bairro, se o cadastro de produtos, o login e a proteção do formulário se comportam como esperado nas situações de maior risco, deixando o resultado registrado e repetível por outra pessoa.

## 3. Escopo

**Será testado:**

- Validação de dados no cadastro de produto
- Acesso a página restrita sem login
- Login com credenciais incorretas
- Proteção do formulário contra requisição forjada (CSRF)
- Exibição segura de texto digitado pelo usuário
- Cadastro de produto com dados válidos

**Não será testado:**

- Registro de vendas e baixa de estoque (testes automatizados na Aula 3)
- Desempenho e carga
- Compatibilidade com outros navegadores
- Publicação em servidor (SA3)

## 4. Ambiente de teste

- Sistema operacional: (informe versão)
- Navegador e versão: (informe)
- Python: 3.10 ou superior
- Flask: versão do `requirements.txt`
- Endereço do sistema: o mostrado pelo terminal ao executar `python app.py`
- Banco: arquivo local, com 5 produtos e 1 usuário de teste

## 5. Tipos de teste

| Tipo | Onde é usado |
| --- | --- |
| Exploratório | Reconhecimento inicial, antes de escrever os casos |
| Manual roteirizado, caixa-preta | CT01 a CT06, executados pela interface |
| Caixa-branca (leitura do código) | Apenas para localizar o defeito quando um caso reprovar |

## 6. Critério de aprovação

O sistema é aprovado nesta etapa quando **os 6 casos têm status Aprovado** e nenhum produto inválido foi gravado no banco durante os testes.

## 7. Casos de teste

### CT01: Cadastro com preço negativo

| Campo | Conteúdo |
| --- | --- |
| ID | CT01 |
| Título | Cadastro com preço negativo |
| Tipo | Manual, caixa-preta |
| Pré-condição | Usuário autenticado; anotar quantos produtos existem em `/produtos` |
| Dados de entrada | Nome `Teste Preço`; preço `-10`; estoque `5`; categoria qualquer |
| Passos | 1. Abrir `/produtos/novo` 2. Preencher os campos com os dados acima 3. Clicar em **Cadastrar produto** 4. Abrir `/produtos` e contar os produtos |
| Resultado esperado | O formulário é reexibido com a mensagem "Informe um preço válido, igual ou maior que zero (ex.: 49,90)." junto do campo preço; os valores digitados continuam preenchidos; a quantidade de produtos na lista não muda |
| Resultado obtido | Formulário reexibido com a mensagem esperada e valores preservados; lista continuou com 5 produtos |
| Status | Aprovado |
| Evidência | `evidencias/ct01-preco-negativo.png` |

### CT02: Acesso a página restrita sem login

| Campo | Conteúdo |
| --- | --- |
| ID | CT02 |
| Título | Acesso a página restrita sem login |
| Tipo | Manual, caixa-preta |
| Pré-condição | Nenhuma sessão aberta (usar janela anônima ou sair do sistema) |
| Dados de entrada | Endereço `/produtos/novo` |
| Passos | 1. Abrir uma janela anônima 2. Digitar o endereço do sistema seguido de `/produtos/novo` 3. Observar a página exibida |
| Resultado esperado | O usuário é redirecionado para `/login` com a mensagem "Acesso restrito. Faça login para continuar."; o formulário de produto **não** aparece |
| Resultado obtido | Redirecionado para a tela de login com a mensagem de acesso restrito |
| Status | Aprovado |
| Evidência | `evidencias/ct02-sem-login.png` |

### CT03: Login com senha errada

| Campo | Conteúdo |
| --- | --- |
| ID | CT03 |
| Título | Login com senha errada |
| Tipo | Manual, caixa-preta |
| Pré-condição | Usuário de teste cadastrado; nenhuma sessão aberta |
| Dados de entrada | Usuário correto (o cadastrado); senha `senhaerrada123` |
| Passos | 1. Abrir `/login` 2. Preencher o usuário correto e a senha errada 3. Clicar em **Entrar** |
| Resultado esperado | Permanece na tela de login com a mensagem genérica "Usuário ou senha incorretos."; a mensagem **não** informa qual dos dois está errado; nenhum acesso é liberado |
| Resultado obtido | Tela de login com a mensagem genérica; acesso negado |
| Status | Aprovado |
| Evidência | `evidencias/ct03-senha-errada.png` |

### CT04: Envio do formulário sem o token CSRF

| Campo | Conteúdo |
| --- | --- |
| ID | CT04 |
| Título | Envio do formulário sem o token CSRF |
| Tipo | Manual, caixa-preta |
| Pré-condição | Usuário autenticado; anotar a quantidade de produtos |
| Dados de entrada | Nome `Teste CSRF`; preço `10,00`; estoque `1`; categoria qualquer; campo oculto `csrf_token` removido |
| Passos | 1. Abrir `/produtos/novo` 2. Abrir as ferramentas do desenvolvedor (F12) e, na aba Elements, localizar `<input type="hidden" name="csrf_token">` 3. Apagar esse campo (ou alterar o valor) 4. Preencher os dados válidos e enviar 5. Conferir `/produtos` |
| Resultado esperado | O servidor responde com erro **403** e a mensagem "Requisição inválida. Recarregue o formulário e tente novamente."; o produto **não** é gravado |
| Resultado obtido | Página de erro 403 com a mensagem esperada; produto ausente da lista |
| Status | Aprovado |
| Evidência | `evidencias/ct04-sem-csrf.png` (mostrar o código de status 403, na aba Network, ou o texto da página) |

### CT05: Produto com HTML no nome

| Campo | Conteúdo |
| --- | --- |
| ID | CT05 |
| Título | Produto com HTML no nome |
| Tipo | Manual, caixa-preta |
| Pré-condição | Usuário autenticado |
| Dados de entrada | Nome `<b>teste</b>`; preço `5,00`; estoque `2`; categoria qualquer |
| Passos | 1. Abrir `/produtos/novo` 2. Preencher com os dados acima 3. Enviar 4. Observar como o nome aparece em `/produtos` |
| Resultado esperado | O produto é cadastrado e o nome aparece **literalmente** como `<b>teste</b>`, sem negrito (o HTML é escapado) |
| Resultado obtido | Nome exibido como texto puro, com os sinais de menor e maior visíveis |
| Status | Aprovado |
| Evidência | `evidencias/ct05-html-escapado.png` |

### CT06: Cadastro com dados válidos

| Campo | Conteúdo |
| --- | --- |
| ID | CT06 |
| Título | Cadastro com dados válidos |
| Tipo | Manual, caixa-preta |
| Pré-condição | Usuário autenticado; anotar quantos produtos existem |
| Dados de entrada | Nome `Mouse sem fio`; preço `89,90`; estoque `20`; categoria `Eletrônicos` |
| Passos | 1. Abrir `/produtos/novo` 2. Preencher com os dados acima 3. Clicar em **Cadastrar produto** 4. Observar a página exibida e a lista |
| Resultado esperado | Redireciona para `/produtos` com o aviso "Produto cadastrado com sucesso."; o novo produto aparece no topo da lista com preço R$ 89,90 e estoque 20; ao apertar F5, nenhum produto é duplicado |
| Resultado obtido | Redirecionado para a lista com o aviso; produto no topo; F5 não duplicou |
| Status | Aprovado |
| Evidência | `evidencias/ct06-cadastro-valido.png` |

%%

---

# Notas do docente

> [!info] Antes da aula
>
> - **Rodar os 6 casos você mesmo** no repositório-base e confirmar mensagens, rotas e códigos. Todas as mensagens acima vêm da nota produtos-06 (Bottle). Se o Flask usar textos diferentes, **corrija o esperado** deste gabarito e da nota `uc3.01`.
> - **CT05 e CT06 gravam dados.** Cada dupla terminará com 2 produtos a mais. Se quiser banco limpo na Aula 2, peça para recriarem o banco ou entregue o script de restauração.
> - **CT01 e CT04 não devem gravar nada.** É o que prova que a validação e o CSRF funcionam: peça que os alunos confiram a **contagem de produtos** antes e depois.

## Onde os alunos costumam errar

| Erro frequente | Como aparece | Como orientar |
| --- | --- | --- |
| Resultado esperado vago | "Dar erro", "não deixar" | Pergunte: "que mensagem? em que lugar da tela? o que acontece com o banco?" |
| Resultado esperado escrito depois da execução | Esperado idêntico ao obtido, palavra por palavra | Peça que escrevam o esperado **antes** de executar |
| Passos não repetíveis | "Cadastrar um produto ruim" | A troca entre duplas expõe o problema: quem executa não consegue seguir |
| CT04 sem remover o token | O envio funciona e o aluno marca Reprovado | Releia o passo 3: o campo precisa ser apagado antes do envio |
| CT02 testado já logado | Abre a página normalmente | Falta a pré-condição: janela anônima ou sair do sistema |
| CT03 usando usuário inexistente | Resultado igual ao esperado, mas o caso testou outra coisa | Discuta: por que o sistema não deve dizer qual dos dois está errado |
| Evidência só com texto | "Funcionou" | Exija captura de tela com o resultado visível |
| Confundir falha e defeito | "O defeito é a tela de erro" | A tela é a falha observada; o defeito é a linha de código |

## Se algum caso reprovar na Aula 1

Trate como oportunidade da própria SA1:

1. Peça a confirmação do passo a passo (pode ser erro do aluno).
2. Se persistir, é **falha real**. Peça o registro em formato de defeito: título, passos, esperado × obtido, evidência.
3. Peça a leitura do trecho do código responsável (caixa-branca) para ligar a **falha** ao **defeito**.
4. Avise a turma para não corrigir o código agora: a correção é o assunto da Aula 6.

## Pontos de observação para a ficha diagnóstica

- Conseguiu criar e ativar o ambiente virtual sem ajuda?
- Leu a mensagem de erro antes de pedir ajuda?
- Usou o terminal e o Git com autonomia?
- Anotou do próprio jeito durante a exploração ou saiu testando sem registrar?

## Lista de verificação para correção (usada na troca entre duplas)

| Critério | Peso sugerido |
| --- | --- |
| Campos completos (ID, título, pré-condição, dados, passos, esperado, obtido, status) | Alto |
| Passos repetíveis por outra pessoa | Alto |
| Resultado esperado verificável e escrito antes | Alto |
| Evidência anexada | Médio |
| Plano de uma página com objetivo, escopo, ambiente e tipos | Médio |
| Critério de aprovação verificável | Baixo |

> [!tip] Sugestão para o feedback imediato
> Comece pelo que a dupla fez bem e use a pergunta do Guia: "o que você acha que pode ser feito para melhorar a clareza dos passos?". Evite "está errado" e prefira "a dupla colega não conseguiu repetir o passo 3 porque...".

%%
