---
quartz-properties: true
title: uc3.01 - Plano de teste e testes manuais
description: Elaboração de um plano de teste e de casos de teste, executados manualmente no sistema Gestão de Produtos
tags:
  - programador-sistemas/aulas/uc3
date: 2026-11-11
uc: 3
aula: 1
---

> [!note] Plano de teste e testes manuais
>
> - Plano de teste e caso de teste (identificação, pré-condição, passos, resultado esperado, resultado obtido, status)
> - Erro, defeito e falha
> - Teste manual, teste exploratório, caixa-preta e caixa-branca
> - Registro de teste
> - [[Python e TDD com flask]]
> - [[roteiro-instalacao-e-execucao|Roteiro de instalação e execução do sistema]]
> - [[modelo-plano-de-teste|Modelo de plano de teste e de caso de teste]]

> [!abstract] Contexto
> A **Loja do Bairro** (caso fictício) vai usar o sistema **Gestão de Produtos** e exige uma garantia de que ele funciona antes de aceitar a entrega. Vocês são a **equipe de qualidade**: precisam mostrar **o que foi testado, como foi testado e com qual resultado**.

> [!todo] 🖥️ Atividades
>
> Trabalhem em **duplas**.
>
> **1. Preparar o sistema**
>
> - Extrair o [repositório-base](https://github.com/jocile/gestao-produtos-base) do sistema Gestão de Produtos e abrir no VS Code.
> - Criar o ambiente virtual e instalar as dependências.
> - Executar o sistema localmente e acessar no navegador.
>
> **2. Explorar o sistema**
>
> - Sua missão é **tentar fazer o sistema falhar**: login, cadastro de produto e lista de produtos.
> - Anote **do seu jeito** o que você fez e o que aconteceu.
>
>> [!question] Questões
>>
>> - Outra pessoa consegue repetir exatamente o que você anotou?
>> - Como você sabia qual era o resultado correto?
>> - O que o sistema fez de errado (**falha**) e qual é a linha de código responsável (**defeito**)?
>
> **4. Escrever o plano e os casos de teste**
>
> - Em `docs/plano-de-teste.md`, escreva o plano de teste de **uma página**: objetivo, escopo, ambiente e tipos de teste.
> - Escreva **6 casos de teste** no formato do modelo abaixo, cobrindo as áreas de risco da tabela.
> - Execute o plano e anote o resultado obtido e o status de cada caso.
>
> **5. Trocar com outra dupla**
>
> - Execute os casos de teste de **outra dupla**, usando somente o texto escrito.
> - Registre resultado esperado × obtido e devolva comentários sobre a clareza dos passos.

> [!info] Modelo de caso de teste
>
> | Campo | Conteúdo |
> | --- | --- |
> | ID | CT01 |
> | Título | Cadastro com preço negativo |
> | Pré-condição | Usuário autenticado |
> | Passos | 1. Acessar `/produtos/novo` 2. Preencher nome "Teste", preço `-10`, estoque `5` e uma categoria 3. Enviar |
> | Resultado esperado | Formulário reexibido com mensagem de erro no campo preço; nada é gravado |
> | Resultado obtido | *(preencher na execução)* |
> | Status | Aprovado / Reprovado |

> [!info] Áreas de risco a cobrir
>
> | ID | Área | Situação a testar |
> | --- | --- | --- |
> | CT01 | Validação do cadastro | Preço negativo |
> | CT02 | Acesso restrito | Abrir `/produtos/novo` sem login |
> | CT03 | Login | Senha errada |
> | CT04 | Proteção do formulário (CSRF) | Enviar o formulário sem o token |
> | CT05 | Exibição de texto | Produto chamado `<b>teste</b>` |
> | CT06 | Cadastro válido | Produto com dados corretos |
>
> Defina o **resultado esperado** de cada caso antes de executá-lo.

> [!tip] Dica para o CT04
> Nas ferramentas do desenvolvedor (F12), apague ou altere o campo oculto `csrf_token` antes de enviar o formulário.

> [!abstract] O que você vai entregar
> O arquivo `docs/plano-de-teste.md`, com:
>
> - plano de teste de uma página (objetivo, escopo, ambiente, tipos de teste)
> - 6 casos de teste, com resultado obtido e status

⬅️ Aula anterior: [[uc2.18 - Gestao de Dados Acessos e Permissoes]] | ➡️ Próxima aula: ✨em edição!
