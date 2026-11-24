---
title: Modelos de Plano de Ação de projeto integrador
description: "modelo de Plano de Ação de projeto integrador."
tags:
  - Projeto-integrador
  - modelo
---

## Modelo de Plano de Ação em Markdown — Projeto Integrador

Below is the **Plano de Ação estruturado** em Markdown para o Projeto Integrador do curso **Técnico em Programador de Sistemas**, desenvolvido em conformidade com as diretrizes do **Modelo Pedagógico Senac (MPS)**.

---

## PLANO DE AÇÃO DO PROJETO INTEGRADOR (UCPI)

## 1. Identificação Geral

* **Curso:** Técnico em Programador de Sistemas (Carga Horária Total: 200h)
* **Unidade Curricular:** Projeto Integrador (Natureza Diferenciada / Correquisito das demais UCs)
* **Docente Responsável pelo PI:** Prof.(a) [Nome do Docente da UCPI]
* **Equipe de Docentes Apoiadores:** Docentes das UCs 1, 2 e 3
* **Tema Gerador:** *"Transformação Digital e Automação de Processos para o Fortalecimento de Pequenos Negócios e Organizações Comunitárias"*
* **Entidade Parceira / Contexto Local:** Microempresas, ONGs ou Projetos Comunitários da região

---

## 2. Objetivos e Marcas Formativas Mobilizadas

* **Objetivo Geral:** Projetar, desenvolver, testar e publicar uma aplicação web funcional, acessível e segura que automatize processos operacionais de uma instituição ou pequeno negócio local, integrando as competências do Perfil Profissional de Conclusão.
* **Marcas Formativas Senac Mobilizadas:**
  * **Domínio Técnico-Científico:** Aplicação de algoritmos, modelagem de dados relacional, arquitetura de software web e suíte de testes automatizados.
  * **Visão Crítica:** Diagnóstico assertivo das necessidades do cliente e análise de viabilidade técnica das soluções.
  * **Atitude Empreendedora e Sustentável:** Otimização de recursos operacionais e geração de impacto socioeconômico positivo.
  * **Atitude Colaborativa e Comunicação:** Trabalho em equipe, mediação de conflitos via versionamento Git/GitHub e diálogo transparente com a comunidade.

---

## 3. Cronograma Executivo e Entregas Parciais por UC

O desenvolvimento do Projeto Integrador articula-se com as demais Unidades Curriculares do curso, as quais fornecem os insumos teóricos e práticos necessários:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        CRONOGRAMA INTEGRADO DO PLANO DE AÇÃO                           │
├──────────────────────┬──────────────────────┬───────────────────┬──────────────────────┤
│  FASE 1: DIAGNÓSTICO │  FASE 2: BANCO DE    │ FASE 3: WEB, TDD  │  FASE 4: SÍNTESE E   │
│  E REQUISITOS (UC1)  │  DADOS & CRUD (UC2)  │  E GITHUB (UC3)   │  DEPLOY (UCPI)       │
└──────────────────────┴──────────────────────┴───────────────────┴──────────────────────┘
```

### Fase 1: Problematização, Requisitos e Lógica do Sistema (Suporte da UC1)

* **Foco da UC1 (Desenvolver algoritmos):** Identificação de necessidades, levantamento de requisitos de software e estruturação da lógica orientada a objetos.
* **Ações dos Alunos:**
  1. Entrevistar o parceiro local (ou simular a dor do cliente) para mapear processos manuais.
  2. Documentar os requisitos funcionais e desenhar os protótipos de interface (*wireframes*).
  3. Estruturar o diagrama de classes e os algoritmos em Python que resolvem as regras de negócio.
* **Entregável Parcial (Marco 1):** Documento de Requisitos + Diagrama de Classes + Protótipos de Tela.
* **Responsáveis:** Alunos (em equipes) sob orientação do docente da UC1 e validação na UCPI.

### Fase 2: Persistência e Banco de Dados Relacional (Suporte da UC2)

* **Foco da UC2 (Desenvolver banco de dados e aplicações):** Modelagem conceitual, lógica e física de dados e construção de rotinas de manipulação.
* **Ações dos Alunos:**
  1. Desenhar o Modelo Entidade-Relacionamento (MER/DER) da aplicação.
  2. Escrever os scripts SQL (DDL) para criação das tabelas e chaves de integridade.
  3. Implementar a camada de acesso a dados (CRUD) conectando o Python ao SGBD.
* **Entregável Parcial (Marco 2):** Script SQL do Banco de Dados + Camada de Persistência (CRUD) testada.
* **Responsáveis:** Alunos sob orientação do docente da UC2.

### Fase 3: Desenvolvimento Web, TDD e Versionamento (Suporte da UC3)

* **Foco da UC3 (Realizar testes e manutenção / Aplicações Web):** Arquitetura web (Flask/Django), testes automatizados (Pytest) e controle de versão no GitHub.
* **Ações dos Alunos:**
  1. Construir os endpoints da API web / rotas do sistema em Flask ou Django.
  2. Desenvolver os testes automatizados (TDD) para garantir cobertura do código-fonte.
  3. Organizar o repositório no GitHub com *branches* de trabalho e publicar a tag da versão estável (`v1.0.0`).
* **Entregável Parcial (Marco 3):** Aplicação Web funcional com testes unitários/integração aprovados e repositório Git atualizado.
* **Responsáveis:** Alunos sob orientação do docente da UC3 e acompanhamento do docente do PI.

### Fase 4: Síntese e Apresentação Pública dos Resultados (Conclusão na UCPI)

* **Foco da UCPI:** Consolidação dos resultados, avaliação final e socialização dos produtos.
* **Ações dos Alunos:**
  1. Realizar a publicação (*deploy*) da aplicação web em servidor ou plataforma online (ex: PythonAnywhere).
  2. Elaborar o Manual do Usuário e consolidar a documentação do projeto.
  3. Apresentar publicamente o sistema em funcionamento (*Pitch*) para a banca, colegas e parceiros da comunidade.
* **Entregável Final (Marco 4):** Aplicação em Produção + Repositório no GitHub + Memorial Reflexivo e Apresentação do Pitch.
* **Responsáveis:** Alunos e Docente do PI, com presença da equipe pedagógica e convidados.

---

## 4. Matriz de Acompanhamento e Monitoramento do Cronograma

| Etapa / Marco | Atividades Principais | UC Vinculada | Carga Horária | Produto / Entregável | Status / Validação |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Etapa I: Problematização** | Validação do Tema Gerador e mapeamento das necessidades | UCPI / UC1 | 8h | Plano de Ação detalhado e Requisitos | [ ] Validado |
| **Marco 1** | Modelagem da Lógica de Negócio e Classes | UC1 | 16h | Protótipo de Telas + Diagrama UML | [ ] Entregue |
| **Marco 2** | Projeto do Banco de Dados e Conexão CRUD | UC2 | 20h | Diagrama DER + Scripts SQL testados | [ ] Entregue |
| **Marco 3** | Desenvolvimento Web, TDD e GitHub | UC3 | 24h | Código Flask/Django + Testes Pytest + Git | [ ] Entregue |
| **Etapa IV: Síntese** | Deploy, Relatório Final e Apresentação Pública | UCPI | 12h | Sistema Publicado + Pitch de Apresentação | [ ] Concluído |

---

## 5. Instrumentos de Avaliação e Acompanhamento Formativo

A avaliação é **processual, contínua e formativa**, apoiada nos seguintes instrumentos:

1. **Ficha de Acompanhamento do Plano de Ação:** Utilizada pelo docente do PI para verificar o cumprimento de prazos e o engajamento individual/coletivo nas entregas parciais.
2. **Rubricas de Avaliação Técnica dos Entregáveis:** Avaliação dos scripts SQL, da arquitetura do código em Python e do percentual de cobertura dos testes em Pytest.
3. **Ficha de Avaliação dos Indicadores do PI:** Registro oficial do atendimento aos 3 indicadores normativos do Projeto Integrador e observação das Marcas Formativas Senac.
4. **Relatório de Autoavaliação e Reflexão Crítica:** Espaço para o estudante analisar sua trajetória, identificar falhas, ressignificar aprendizados e avaliar o trabalho em equipe.

---

## 6. Recursos Didáticos Necessários

* Laboratório de Informática equipado com Python 3.x, IDE VSCode e banco de dados SQLite/MySQL.
* Acesso à internet para versionamento no GitHub e hospedagem de testes (ex: PythonAnywhere).
* Projetor multimídia para as reuniões de alinhamento e apresentação final do Pitch.
* Modelos e templates de documentos técnicos de requisitos e planilhas de testes.

---

🛠️ [[Rubrica de Avaliacao PI programador|rubrica de avaliação em formato de tabela]] para analisar os projetos entregues no GitHub!
