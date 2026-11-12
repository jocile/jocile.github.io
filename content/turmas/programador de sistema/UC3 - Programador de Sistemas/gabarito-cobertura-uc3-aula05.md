---
title: Gabarito - Análise e cobertura da Aula 5 da UC3 (uso do docente)
description: Cálculos, ordem de correção, comandos e testes de cobertura, estimativa do relatório, análise em 5 linhas e rubrica da uc3.05. Não publicar.
date: 2026-11-17
draft: true
tags:
  - programador-sistemas/gabarito
  - uc3
---

> [!warning] Uso exclusivo do docente
> Não publicar. As cifras de cobertura abaixo são **estimativas** com base no código Bottle da UC2. **Rode `pytest --cov` no repositório-base com a v0.9 e substitua** os números pela saída real antes de usar em sala.

## 0. Preparação

### Dependências

```text
# requirements.txt (acrescentar, se não houver)
pytest-cov
```

Os alunos que ainda não instalaram usam `pip install pytest-cov`. Entregue o `.coveragerc` da nota já pronto no repositório-base para evitar medir `tests/` e `.venv/`.

```ini
[run]
branch = True
source = .
omit =
    tests/*
    .venv/*

[report]
show_missing = True
```

> [!bug] Por que `omit`
> Sem ele, o relatório inclui os próprios testes e arquivos do ambiente virtual, e o percentual perde o sentido (os testes sempre têm 100%).

### Comando

```bash
pytest --cov --cov-report=term-missing --cov-report=html
```

> [!info] Testes que falham não impedem a cobertura
> Com a v0.9, 3 testes falham, mas o pytest-cov **mede mesmo assim**. Avise a turma: o relatório sai com `FAILED` no topo e isso é esperado.

## 1. Cálculos da taxa de aprovação (só testes obrigatórios)

| Conjunto | Aprovados | Total | Taxa |
| --- | --- | --- | --- |
| Casos manuais (CT01 a CT06) | 4 | 6 | 66,7% |
| Testes automatizados | 10 | 13 | 76,9% |
| Todos | 14 | 19 | 73,7% |

Cada dupla terá números próprios se escreveu testes opcionais. O que se confere é o **método** (aprovados ÷ total × 100), não o número idêntico.

## 2. Ordem de correção (aceitar variações justificadas)

| Ordem | Defeito | Severidade | Prioridade | Justificativa |
| --- | --- | --- | --- | --- |
| 1 | DEF-01: venda sem baixa e sem erro | Crítica ou Alta | Alta | Corrompe estoque e faturamento, e **só a suíte automatizada o detectou** |
| 2 | DEF-02: novo produto sem login | Média | Alta | Correção simples e exposição de funcionalidade interna |
| 3 | DEF-03: preço negativo na validação | Baixa | Média | O banco ainda impede a gravação; o dano é só a mensagem |

> [!info] Variações aceitáveis
> DEF-02 em primeiro lugar, por ser rápido e de segurança. Peça que a dupla justifique pela **combinação** de severidade e prioridade, e não apenas pelo número do defeito. Rejeite justificativas do tipo "foi o primeiro que apareceu".

## 3. Estimativa do relatório de cobertura (v0.9 + testes das Aulas 2 e 3)

> [!warning] Estimativa, não resultado
> Confirme com a execução real.

| Arquivo | Cobertura estimada | O que provavelmente fica de fora |
| --- | --- | --- |
| `validacao.py` | Muito alta (≈ 95 a 100%) | Quase tudo é executado pelos 6 testes |
| `seguranca.py` | Muito alta (≈ 100%) | `gerar_hash_senha` e `verificar_senha` são chamadas |
| `dados.py` | Média | `consultar_ranking` (só o relatório e a API usam) e `inserir_produto` (só o POST válido usa) |
| `app.py` | Média | Rota do relatório e da API de ranking, logout, rota de arquivos estáticos e o caminho de sucesso do `POST /produtos` |
| **Total** | Entre 70 e 85% de linhas | Com `branch = True`, o número cai alguns pontos |

> [!info] Hipóteses esperadas dos alunos
> Os alunos tendem a apontar **"as rotas"** e **"o relatório"**. É uma boa hipótese. Os que sugerem "a validação" erram, e é produtivo: a validação tem as linhas **mais cobertas**.

### Seguindo a pergunta-guia

- **"Como confirmar a sua hipótese?"** Medindo: o pytest-cov mostra **quais linhas** rodaram.
- **"100% de cobertura garante um sistema sem defeitos?"** Não. Use a demonstração da seção 4.

## 4. Demonstração: cobertura não é qualidade

Mostre este relatório no seu computador e mande a turma procurar:

1. Abra `htmlcov/dados_py.html` (ou o equivalente) e vá até `registrar_venda` da v0.9.
2. As linhas do `INSERT`, do `if` e do `UPDATE` estão **verdes** (executadas), pois os testes 1 e 2 da Aula 3 as exercitam.
3. Mesmo assim, o **DEF-01 está nessa função** e o teste 2 **falha**.
4. Faça o mesmo em `validacao.py`: a linha com `math.isfinite` está verde, e é ali que está o DEF-03.

> [!question] Perguntas para a turma
> - As linhas dos defeitos estavam vermelhas ou verdes? (**verdes**)
> - Se a cobertura mede o que rodou, por que ela não encontrou o defeito? (porque ela não mede se o resultado é **correto**)
> - Então qual é o papel do `assert`? (**verificar**; a cobertura só aponta onde ninguém verificou)
>
> Fecha o tema: cobertura mostra **o que não foi testado**, e não **o que está certo**.

### Demonstração do "teste que sobe número e não protege"

```python
# NÃO fazer: executa a linha e não verifica nada
def test_ranking_so_para_subir_cobertura(cliente_logado):
    cliente_logado.get("/relatorio/ranking")
```

Rode a cobertura: sobe. Agora sabote a rota (por exemplo, retorne uma página vazia): **o teste continua passando**. Compare com o teste que confere o conteúdo da resposta (seção 5).

## 5. Gabarito dos testes novos (`tests/test_cobertura.py`)

Os testes abaixo cobrem trechos **sem relação** com os 3 defeitos da v0.9, então devem **passar**. Estão apoiados nas fixtures do `conftest.py` da Aula 3.

```python
from conftest import SENHA_TESTE, USUARIO_TESTE


def test_cadastro_valido_grava_produto_e_redireciona(
    cliente_logado, obter_token_csrf, banco
):
    # Preparar
    dados_form = {
        "csrf_token": obter_token_csrf(),
        "nome": "Mouse sem fio",
        "preco": "89,90",
        "estoque": "20",
        "id_categoria": "1",
    }

    # Executar
    resposta = cliente_logado.post("/produtos", data=dados_form)

    # Verificar
    assert resposta.status_code == 302
    assert "/produtos" in resposta.headers["Location"]

    produto = banco.execute(
        "SELECT preco, estoque FROM Produto WHERE nome = ?;", ("Mouse sem fio",)
    ).fetchone()
    assert produto is not None
    assert produto["preco"] == 89.9
    assert produto["estoque"] == 20
    assert banco.execute("SELECT COUNT(*) FROM Produto;").fetchone()[0] == 6


def test_api_de_ranking_devolve_todos_os_produtos(cliente):
    resposta = cliente.get("/api/ranking-vendas")

    assert resposta.status_code == 200
    corpo = resposta.get_json()
    assert corpo["status"] == "sucesso"
    assert len(corpo["dados"]) == 5
    assert {"produto", "total_vendido", "estoque_restante"} <= set(corpo["dados"][0])
```

### Testes extras (para quem terminar antes)

```python
def test_relatorio_de_ranking_exige_login(cliente):
    resposta = cliente.get("/relatorio/ranking")

    assert resposta.status_code == 302
    assert "/login" in resposta.headers["Location"]


def test_relatorio_de_ranking_mostra_os_produtos_apos_login(cliente_logado):
    resposta = cliente_logado.get("/relatorio/ranking")

    assert resposta.status_code == 200
    pagina = resposta.get_data(as_text=True)
    assert "Smartphone" in pagina
    assert "Camisa Polo" in pagina


def test_login_com_senha_errada_nao_libera_o_acesso(cliente):
    resposta = cliente.post(
        "/login", data={"usuario": USUARIO_TESTE, "senha": "senhaerrada123"}
    )

    assert resposta.status_code == 302
    assert "erro=invalido" in resposta.headers["Location"]

    # A sessão não foi criada: a lista continua restrita
    lista = cliente.get("/produtos")
    assert lista.status_code == 302


def test_login_de_usuario_inexistente_nao_libera_o_acesso(cliente):
    resposta = cliente.post(
        "/login", data={"usuario": "ninguem", "senha": SENHA_TESTE}
    )

    assert resposta.status_code == 302
    assert "erro=invalido" in resposta.headers["Location"]
```

> [!bug] Suposições sobre o Flask
> - `consultar_ranking()` e a rota `/api/ranking-vendas` existem como na nota `produtos-04`. Confirme se o Flask devolve JSON com `jsonify` ou `dict` e ajuste `resposta.get_json()`.
> - O parâmetro `erro=invalido` vem do `ir_para_login("invalido")` da nota `produtos-05`.
> - O redirecionamento do `POST /produtos` válido é `/produtos?ok=cadastrado`. O teste só confere que contém `/produtos`.

### Resultado esperado depois dos testes novos

```text
tests/test_cobertura.py ..  (ou ......, com os extras)
```

**Quatro testes extras mais os dois obrigatórios** aumentam a cobertura em `app.py` e `dados.py`, e a meta de 80% de linhas costuma ser atingida. Se um aluno chegar a 80% **só com** o `test_cadastro_valido...`, confira se a justificativa do que ficou de fora é coerente.

> [!info] Quando não chega a 80%
> Peça a justificativa por escrito do que ficou de fora, usando as três perguntas da nota (impacto, facilidade, valor de verificação). Linhas de `if __name__ == "__main__":` e do arquivo estático costumam ser omissões razoáveis.

## 6. Análise em 5 linhas (gabarito)

1. Dos 19 casos, 14 passaram (73,7%), mas as 3 falhas estão em **venda**, **acesso** e **cadastro de produto**, áreas de impacto alto para a loja.
2. O maior risco é a venda registrada sem baixa de estoque, porque corrompe o estoque e o faturamento sem gerar nenhum erro visível.
3. A cobertura mostrou que o relatório e a API de ranking nunca eram executados, e os casos manuais da Aula 1 também não os cobriam.
4. Os testes não provam que o sistema suporta muitos usuários ao mesmo tempo, e cobertura alta não garante que todos os resultados estejam corretos: as linhas dos defeitos já eram executadas.
5. Recomendamos corrigir a venda e o acesso antes da entrega e manter a suíte rodando a cada versão.

## 7. Erros frequentes

| Erro | Como aparece | Como orientar |
| --- | --- | --- |
| Teste sem `assert` | Cobertura sobe, o teste nunca falha | Faça a **sabotagem** da seção 4: o teste continua verde |
| Cobertura do `tests/` | 100% enganoso | Falta `omit` no `.coveragerc` |
| Confundir linhas e ramos | Dupla fala 85% e outra 78% | Uma ligou `branch = True` e a outra não; compare sob o mesmo critério |
| Corrigir o defeito "já que está aqui" | Altera `dados.py` | Lembre: corrigir é a Aula 6 |
| Cobertura usada como meta absoluta | "Precisamos de 100%" | Peça a justificativa do que é de baixo valor testar |
| Taxa calculada com todos os testes **e** casos como se fossem uma lista | Soma errada | O total é aprovados ÷ total da soma dos dois conjuntos |
| Análise só com números | "73,7% passaram" | Peça **risco** e **recomendação** |
| Commit com `htmlcov/` e `.coverage` | Pasta enorme no repositório | `git add` apenas de `tests/`, `docs/` e `.coveragerc`; o `.gitignore` entra na Aula 7 |

## 8. Cronograma sugerido (240 min)

| Tempo | Atividade |
| --- | --- |
| 0 a 40 min | Taxa de aprovação, ordem de correção e hipótese |
| 40 a 80 min | Demonstração do pytest-cov, relatório HTML, limites; consulta à documentação |
| 80 a 195 min | Gerar o relatório, comparar com a hipótese, escrever os testes, medir de novo (≈ 75 min) e registrar (≈ 25 min) |
| 195 a 230 min | Análise em 5 linhas e commit |
| 230 a 240 min | Fechamento: como equipes usam cobertura |

> [!tip] Mercado de trabalho (fechamento)
> Em muitas equipes a cobertura entra como **verificação automática** em cada alteração: se cair abaixo de um limite, o código não é aceito. Pergunte se isso é uma boa ideia, e lembre da demonstração dos testes sem `assert`.

## 9. Menção parcial do Indicador 2 (acompanhamento)

| Critério | A | PA | NA |
| --- | --- | --- | --- |
| **Interpretação dos resultados** | Taxa correta e ordem justificada por severidade e prioridade | Taxa correta, justificativa fraca | Taxa errada ou sem ordem |
| **Uso da cobertura** | Hipótese comparada com o relatório e testes novos com `assert` | Testes novos sem verificação real | Não gerou o relatório |
| **Análise escrita** | 5 linhas com risco, limites e recomendação | Só descreve números | Ausente |

> [!tip] Feedback sugerido
> "Sua análise ligou a taxa de aprovação ao risco de cada falha, e isso mostra que você interpretou o número. Para o próximo passo, diga também o que a cobertura **não** garante."

## 10. O que vem na Aula 6

Na Aula 6 a dupla corrige os 3 defeitos **um por vez**, usando depurador e testes de regressão. A ordem de correção definida hoje é o roteiro, e a cobertura de hoje (**antes**) vira o ponto de comparação da cobertura **depois** das correções.
