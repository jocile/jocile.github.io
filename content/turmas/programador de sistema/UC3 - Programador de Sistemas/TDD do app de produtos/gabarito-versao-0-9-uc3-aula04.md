---
title: Gabarito - Versão 0.9 e registros da Aula 4 da UC3 (uso do docente)
description: Como gerar a versão 0.9 com 3 defeitos, resultado esperado do pytest, tabelas e registros preenchidos e notas de correção da uc3.04. Não publicar.
date: 2026-11-16
draft: true
tags:
  - programador-sistemas/gabarito
  - uc3
---

## 0. Como gerar a `versao-0.9/` para os testes

Rode `gerar_versao_0_9.py` **só sobre a cópia limpa** da versão correta. O script aplica 3 trocas e para com erro se um trecho não for encontrado exatamente uma vez.

| Defeito | Arquivo | Troca |
| --- | --- | --- |
| DEF-03 (preço negativo) | `validacao.py` | `if not math.isfinite(preco) or preco < 0:` → `if not math.isfinite(preco):` |
| DEF-01 (venda sem baixa) | `dados.py` | `registrar_venda` grava a venda e só baixa o estoque se houver saldo, **sem erro** |
| DEF-02 (sem login) | `app.py` | Remove `@login_required` de `exibir_formulario` (`GET /produtos/novo`) |

> [!info] Mensagem que continua prometendo a regra
> Na v0.9 a mensagem "Informe um preço válido, igual ou maior que zero" continua no código, mas a regra deixou de ser aplicada. Bom exemplo para a plenária: o texto **promete** algo que o sistema não cumpre.

## 1. Verificação antes da aula

Com a v0.9 copiada para uma cópia do projeto, rode `pytest -v --tb=short`. São **17 testes**: 13 passam e 4 falham.

| Falha | Defeito |
| --- | --- |
| `test_validacao.py::test_preco_negativo_e_recusado` | DEF-03 |
| `test_integracao.py::test_dados_invalidos_retornam_400` | DEF-03 |
| `test_integracao.py::test_venda_com_estoque_insuficiente_nao_altera_nada` | DEF-01 |
| `test_integracao.py::test_pagina_de_novo_produto_sem_login_redireciona_para_o_login` | DEF-02 |

Mensagens esperadas:

```text
test_preco_negativo_e_recusado    -> assert {'nome': ..., 'preco': -5.0, ...} is None
test_venda_com_estoque_insuficiente... -> Failed: DID NOT RAISE <class 'sqlite3.IntegrityError'>
test_pagina_de_novo_produto_sem_login... -> assert 200 == 302
test_dados_invalidos_retornam_400 -> falha no SEGUNDO assert (texto), não no status
```

> [!info] Por que `test_dados_invalidos_retornam_400` falha pelo texto
> Com a v0.9 o preço `-10` passa pela validação, mas o banco recusa pelo `CHECK(preco >= 0.0)`. O app captura o `IntegrityError` e responde **400** com "O banco de dados recusou os dados informados." Então o **status** (400) está certo, e o que falha é o texto "Informe um preço válido". Nada inválido é gravado, e por isso a severidade do DEF-03 é baixa. A saída do pytest mostra a página HTML inteira, o que é um bom motivo para ensinar a **resumir a mensagem em uma linha** no registro.

> [!warning] Confira antes da aula
> - Onde o formulário mostra a mensagem `geral` (acima dos campos ou junto deles). Anote o texto real para CT01.
> - O `tests/test_rascunho_banco_real.py` **não pode estar** na pasta `tests/`: com a v0.9 ele também falharia e confundiria a contagem.
> - Duas das falhas (DEF-03) têm a mesma causa: é a prova viva da regra "um registro por defeito". Use isso na plenária.


Rode `pytest -v --tb=short` com a v0.9 sobre o projeto completo (SA1 pronta, só testes obrigatórios). Resultado esperado: **13 testes, 10 passam e 3 falham**.

```text
FAILED tests/test_validacao.py::test_preco_negativo_e_recusado
       - assert {'nome': 'Mouse sem fio', 'preco': -5.0, ...} is None
FAILED tests/test_integracao.py::test_venda_com_estoque_insuficiente_nao_altera_nada
       - Failed: DID NOT RAISE <class 'sqlite3.IntegrityError'>
FAILED tests/test_integracao.py::test_pagina_de_novo_produto_sem_login_redireciona_para_o_login
       - assert 200 == 302
```

Com os testes opcionais que alguns alunos escreveram, podem falhar também:

| Teste opcional | Falha por causa de |
| --- | --- |
| `test_preco_logo_abaixo_de_zero_e_recusado` | Defeito 1 |
| Parametrizados `("preco","-5")` e `("preco","-0,01")` | Defeito 1 |
| `test_dados_invalidos_retornam_400` | Defeito 1 (veja o quadro abaixo) |

> [!info] Por que o Defeito 1 aparece "disfarçado" na web
> O banco ainda tem `CHECK(preco >= 0.0)`. Com a v0.9, o produto negativo passa pela validação e o **banco o recusa**. O app captura o `IntegrityError` e devolve **400 com a mensagem genérica** "O banco de dados recusou os dados informados." em vez de "Informe um preço válido...". O teste `test_dados_invalidos_retornam_400` falha pelo **texto da mensagem**, não pelo status. Nada inválido é gravado, e **por isso a severidade é baixa**. Ótimo assunto para a plenária: *defesa em profundidade*, a segunda camada segurou o que a primeira deixou passar.

> [!warning] Os 3 defeitos aparecem de forma diferente
> - **Defeito 1:** nos testes unitários **e** no caso manual CT01.
> - **Defeito 3:** nos testes de integração **e** no caso manual CT02.
> - **Defeito 2:** **só** no teste automatizado. O plano manual da Aula 1 não cobre vendas. Use isso na Aula 5, quando a cobertura mostrar a parte não testada.

### Dica para quem não entender o "DID NOT RAISE"

O teste para no `pytest.raises` e não mostra o que sobrou no banco. Quem pedir ajuda pode escrever um teste de diagnóstico (que **não** é para manter):

```python
# tests/test_diagnostico_venda.py   (apagar depois)
from contextlib import closing

import dados


def test_diagnostico_venda(banco):
    with closing(dados.abrir_conexao()) as conn:
        dados.registrar_venda(conn, 3, 100)

    estoque = banco.execute("SELECT estoque FROM Produto WHERE id_produto = 3;").fetchone()[0]
    vendas = banco.execute("SELECT COUNT(*) FROM Vendas;").fetchone()[0]
    print("estoque:", estoque, "| vendas:", vendas)
```

Execute com `pytest -s tests/test_diagnostico_venda.py`: aparece `estoque: 3 | vendas: 1`. Essa é a **falha completa**: venda registrada, estoque inalterado, nenhum erro.

## 2. `docs/resultados-de-teste.md` (gabarito, só testes obrigatórios)

**Versão 0.9, ambiente local.**

| Caso | Título | Obtido | Status |
| --- | --- | --- | --- |
| CT01 | Preço negativo | Formulário reexibido (400) com a mensagem genérica do banco; sem mensagem no campo preço; nada gravado | **Reprovado** |
| CT02 | Acesso sem login | Formulário de novo produto exibido sem login | **Reprovado** |
| CT03 a CT06 | Senha errada, CSRF, HTML escapado, cadastro válido | Como esperado | Aprovados |

| Arquivo | Total | Passaram | Falharam |
| --- | --- | --- | --- |
| tests/test_validacao.py | 8 | 7 | 1 |
| tests/test_seguranca.py | 3 | 3 | 0 |
| tests/test_integracao.py | 6 | 3 | 3 |

**Números para a Aula 5** (variam conforme os testes opcionais de cada dupla):

| Conjunto | Aprovados ÷ total | Taxa |
| --- | --- | --- |
| Casos manuais | 4 ÷ 6 | 66,7% |
| Testes automatizados | 13 ÷ 17 | 76,5% |
| Todos | 17 ÷ 23 | 73,9% |

## 3. `docs/registro-de-defeitos.md` (gabarito)

| ID | Defeito | Casos relacionados | Severidade | Prioridade |
| --- | --- | --- | --- | --- |
| DEF-01 | Venda com estoque insuficiente é registrada, sem baixa e sem erro | `test_venda_com_estoque_insuficiente...` | Crítica ou Alta | Alta |
| DEF-02 | Página de novo produto abre sem login | CT02; `test_pagina_de_novo_produto_sem_login...` | Média | Alta |
| DEF-03 | Validação aceita preço negativo | CT01; `test_preco_negativo...`; `test_dados_invalidos...` | Baixa | Média |

O DEF-01 só aparece na suíte automatizada: o plano manual da Aula 1 não cobre vendas. Guarde isso para a Aula 5.

Os passos para reproduzir e as justificativas de severidade são os mesmos do gabarito anterior. O DEF-01 deve usar o teste de diagnóstico da resposta passada (`registrar_venda(banco_temporario, 3, 100)`), que na v0.9 imprime `estoque: 3 | vendas: 1`.

### DEF-01: Venda com estoque insuficiente é registrada sem baixa e sem erro

| Campo | Conteúdo |
| --- | --- |
| Versão | 0.9 |
| Rota ou módulo | Registro de vendas (`dados.py`, suspeita) |
| Casos relacionados | `test_venda_com_estoque_insuficiente_nao_altera_nada` |
| Passos para reproduzir | 1. Com o banco de teste, escolher o Sofá (estoque 3) 2. Registrar uma venda de 100 unidades 3. Conferir o estoque e a tabela `Vendas` |
| Resultado esperado | Venda recusada com erro; estoque continua 3; nenhuma venda registrada |
| Resultado obtido | Venda aceita **sem erro**; estoque continua 3; **1 venda registrada** |
| Severidade | **Crítica** (ou Alta) |
| Justificativa | Vendas registradas sem baixa tornam o estoque e o faturamento inconsistentes |
| Prioridade | Alta |
| Status | Aberto |

### DEF-02: Página de novo produto abre sem login

| Campo | Conteúdo |
| --- | --- |
| Versão | 0.9 |
| Rota ou módulo | `/produtos/novo` (`app.py`, suspeita) |
| Casos relacionados | CT02; `test_pagina_de_novo_produto_sem_login_redireciona_para_o_login` |
| Passos para reproduzir | 1. Abrir uma janela anônima 2. Acessar `/produtos/novo` |
| Resultado esperado | Redirecionamento para `/login` |
| Resultado obtido | Formulário exibido (200) sem autenticação |
| Severidade | **Média** |
| Justificativa | O formulário fica exposto a qualquer pessoa, mas o envio continua protegido por login e CSRF |
| Prioridade | Alta |
| Status | Aberto |

### DEF-03: Cadastro aceita preço negativo na validação

| Campo | Conteúdo |
| --- | --- |
| Versão | 0.9 |
| Rota ou módulo | Cadastro de produto (`validacao.py`, suspeita) |
| Casos relacionados | CT01; `test_preco_negativo_e_recusado` |
| Passos para reproduzir | 1. Fazer login 2. Abrir `/produtos/novo` 3. Preencher preço `-10` e dados válidos 4. Enviar |
| Resultado esperado | Mensagem de preço inválido junto do campo; nada gravado |
| Resultado obtido | Mensagem genérica do banco no topo; nada gravado |
| Severidade | **Baixa** |
| Justificativa | O banco recusa o dado, então nada inválido é gravado; o usuário só recebe uma mensagem pouco clara |
| Prioridade | Média |
| Status | Aberto |

> [!info] Ordem de correção para a Aula 5
> Sugestão: **DEF-01 → DEF-02 → DEF-03**. Aceite outras ordens bem justificadas, como DEF-02 primeiro por ser a correção mais simples. O ponto da aula é separar **severidade** de **prioridade**.

## 4. Erros frequentes

| Erro | Como aparece | Como orientar |
| --- | --- | --- |
| Um registro por linha vermelha | 4 ou 5 "defeitos" | Pergunte: "o CT01 e o teste do preço negativo descrevem o mesmo comportamento?" |
| Defeito descrito como a mensagem do teste | "Defeito: `assert 200 == 302`" | Isso é a **falha**; a pergunta é qual comportamento está errado |
| Severidade igual à prioridade, sempre | Tudo "Alta/Alta" | Use o exemplo do DEF-03: pouco impacto, mas precisa corrigir |
| Passos que dependem de contexto | "Fazer o teste que falhou" | A dupla colega não consegue reproduzir |
| Esperado e obtido iguais | O aluno escreveu o obtido igual ao esperado | Peça a evidência |
| Só a falha do pytest para o DEF-01 | "DID NOT RAISE" como resultado obtido | Estimule o teste de diagnóstico |
| Abriu o código e já quer corrigir | Edita `dados.py` na Aula 4 | Lembre: corrigir é a Aula 6; hoje é observar e registrar |
| Resultados só dos manuais | Esquece a suíte | A tabela tem duas seções |

## 5. Cronograma sugerido (240 min)

| Tempo | Atividade |
| --- | --- |
| 0 a 50 min | Substituir os arquivos, executar `pytest` e os casos manuais, anotar livremente |
| 50 a 110 min | Perguntas-guia, modelos de resultados e de defeito, severidade × prioridade; plenária comparando as anotações livres com os modelos |
| 110 a 195 min | Preencher resultados e defeitos (≈ 45 min); trocar e reproduzir com a outra dupla (≈ 40 min) |
| 195 a 230 min | Ajustes e commit |
| 230 a 240 min | Fechamento: como equipes de qualidade registram defeitos no mercado |

> [!tip] Quando liberar os modelos
> A 1ª ação é "anotar do seu jeito". Publique `modelo-resultados-de-teste` e `modelo-registro-de-defeitos` **só no momento da reflexão**, ou peça aos alunos que não os abram antes. O contraste entre o registro livre e o modelo é o ponto da plenária.

## 6. Menção parcial do Indicador 2 (acompanhamento)

*Tabula o resultado, de acordo com as informações obtidas no teste realizado.*

| Critério | A | PA | NA |
| --- | --- | --- | --- |
| **Tabela de resultados** | Todos os casos e testes, versão e data, esperado × obtido específico | Falta algum caso, ou obtido vago | Tabela incompleta ou sem relação com o que foi executado |
| **Registro de defeitos** | Um por defeito distinto, passos reproduzíveis, severidade justificada | Registro por falha (não por defeito), ou severidade sem justificativa | Registros sem passos ou sem esperado × obtido |
| **Reprodutibilidade** | A dupla colega reproduziu todos sem ajuda | Reproduziu com perguntas à dupla | Não conseguiu reproduzir |

Registre como **acompanhamento** (A, PA ou NA), com feedback imediato. A menção oficial do indicador vem na Avaliação 2, na Aula 6.

> [!tip] Feedback sugerido
> "Seu registro permitiu que a outra dupla chegasse ao passo 4 sem perguntar nada. Para o próximo passo, justifiquem a severidade em uma frase: o que acontece de ruim se o defeito chegar ao cliente?"

## 7. O que vem na Aula 5

Cada dupla terá resultados e defeitos próprios. Na Aula 5 usam a tabela para calcular a **taxa de aprovação**, propor a **ordem de correção** e gerar o **relatório de cobertura**. O DEF-01, que só a suíte automatizada pegou, tende a aparecer como "parte pouco testada": guarde essa conversa.
