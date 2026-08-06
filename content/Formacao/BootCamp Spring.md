---
class: classe-formacao
description: Lista de disciplinas da formação com sistemas em Java
status: ✅ Concluído
horas-aula: 160
habilidades:
  - Java
  - SpringBoot
  - TDD
  - JUnit
link: "[Prof. Nelio Alves - Devsuperior: Escola de Programação](https://devsuperior.com.br/)"
certificado: "![[BootCamp Spring.png]]"
started: 2021-11-15
finished: 2024-01-23
tags:
  - Formação
  - Java
title: BootCamp Spring
---
# BootCamp Spring React

>[!check]- Desafios de projeto:
> - [x] [API CRUD de clientes](https://github.com/jocile/dsclient)
> - [x] [TDD Event-City](https://github.com/jocile/bds02)
> - [x] [Validação e segurança](https://github.com/jocile/bds04)
> - [x] [MovieFlix domínio e autorização](https://github.com/jocile/bds05)
> - [x] [MovieFlix casos de uso](https://github.com/jocile/movieflix)
> - [Repositórios dos desafios do BootCamp](https://github.com/search?q=org%3Adevsuperior+bds&type=repositories)

> [!summary]- 01 CRUD
> -  01-01 Visão geral do capítulo
> - 01-02 Visão geral do ecossistema Spring
> - 01-03 Aviso sobre o processo de desenvolvimento
> - 01-04 Visão geral do app dscatalog
> - 01-05 Instalação das ferramentas
> - 01-06 Criação do projeto Spring Boot
> - 01-07 Salvando o projeto no Github
> - 01-08 Classe Category
> - 01-09 Category Resource
> - 01-10 Observações importantes sobre o sistema
> - 01-11 Banco de dados H2, camadas
> - 01-12 Transações e sessão JPA
> - 01-13 Seeding da base de dados
> - 01-14 DTO
> - 01-15 Criando um ambiente de execução no Postman
> - 01-16 Buscando categoria por id
> - 01-17 Tratamento de exceções
> - 01-18 Inserindo nova categoria com POST
> - 01-19 Atualizando categoria com PUT
> - 01-20 Deletando categoria com DELETE
> - 01-21 Dados de auditoria
> - 01-22 Paginação
> - 01-23 Entidade Product, revisão modelo relacional N-N
> - 01-24 Mapeamento JPA N-N, script SQL completo
> - 01-25 ProductDTO
> - 01-26 Product repository, service, resource, GET
> - 01-27 Product insert, update, delete
> - 01-28 Apresentando o trabalho final do capítulo

> [!summary]- 02 Testes automatizados
> - 02-01 Visão geral do capítulo
 > - 02-02 Tipos de teste
 > - 02-03 Benefícios dos testes automatizados
 > - 02-04 O que é TDD
 > - 02-05 Boas práticas para testes
 > - 02-06 Visão geral do JUnit
 > - 02-07 Primeiro teste na prática com JUnit
 > - 02-08 Observação sobre TDD
 > - 02-09 Teste deposito deveria fazer nada quando quantia for negativa
 > - 02-10 Padrão de projeto Factory para instanciar objetos
 > - 02-11 Teste saque total deveria limpar saldo e retornar todo saldo
 > - 02-12 Testes para método withdraw
 > - 02-13 Exercício JUnit vanilla
 > - 02-14 Baixando o projeto do capítulo 1 (se precisar)
 > - 02-15 Refatoração no Pageable
 > - 02-16 Visão geral de testes com Spring, principais annotations
 > - 02-17 Primeiro teste de repository
 > - 02-18 Testando outro cenário do delete
 > - 02-19 Fixtures no JUnit, BeforeEach
 > - 02-20 Testando save com id nulo
 > - 02-21 Exercício com repository
 > - 02-22 Começando testes de ProductService, Mockito vs MockBean
 > - 02-23 Primeiro teste, simulando comportamento com Mockito
 > - 02-24 Imports estáticos do Mockito
 > - 02-25 Teste delete lança ResourceNotFoundException quando id não existe
> - 02-26 Teste delete lança DatabaseException quando id dependente
> - 02-27 Simulando comportamentos diversos com Mockito
> - 02-28 Testando findAllPaged do ProductService
> - 02-29 Exercício testes de unidade com Mockito
> - 02-30 Começando testes na camada web
> - 02-31 Legibilidade e negociação de conteúdo
> - 02-32 Testando o findById
> - 02-33 Testando o update
> - 02-34 Simulando outros comportamentos do ProductService
> - 02-35 Exercício testes na camada web
> - 02-36 Nosso primeiro teste de integração
> - 02-37 Teste de integração para findAllPaged
> - 02-38 Teste de integração na camada web findAll
> - 02-39 Teste de integração na camada web update
> - 02-40 Apresentando o desafio TDD resolvido
> - 02-41 Implementando o desafio resolvido
> - 02-42 Desafio TDD para entregar
> - TAREFA: TDD Event-City

> [!summary]- 03 - Validação e segurança
> - 03-01-3 Visão geral do capítulo
> - 03-02 Baixando o projeto pronto ao final deste capítulo
> - 03-03 Baixando o projeto do capítulo anterior (se precisar)
> - 03-04 Implementando entidades User e Role
> - 03-05 Mapeamentos objeto-relacional, seed do banco
> - 03-06-8 CRUD de usuários 
> - 03-07 CRUD de usuários Classe de configuração - componentes @ Bean Spring Security - senha
> - 03-08 CRUD de usuários UserRespository (controller)
> - 03-09 Introdução ao Bean Validation
> - 03-10 Testando anotações básicas
> - 03-11,12 Tratando exceção MethodArgumentNotValidException
> - 03-12 Resposta customizada para erro de validação
> - 03-13 Implementando um ConstraintValidator customizado
> - 03-14,15 UserUpdateValidator 
> - 03-15 UserUpdateValidator 
> - 03-16 Token JWT, autenticação e autorização
> - 03-17 OAuth2
> - 03-18 Como funciona o processo de login
> - 03-19 Checklist do Spring Security
> - 03-20 Checklist do Spring OAuth e JWT
> - 03-21 Ajustando o arquivo pom.xml
> - 03-22 Implementando checklist do Spring Security
> - 03-23 Implementando OAuth2 authorization server
> - 03-24 Externalizando configuração, variáveis de ambiente
> - 03-25 Adicionando informações ao token
> - 03-26 Implementando OAuth2 resource server
> - 03-27 Configuração especial para o banco H2
> - 03-28 Deixando o Postman top
> - 03-29 Spoiler - próximos tópicos de autenticação e autorização
> - 03-30 Apresentando o desafio resolvido
> - 03-31 Reaproveitando a infraestrutura do DSCatalog
> - 03-32 Implementando as funcionalidades
> - 03-33 Desafio para entregar
> - 03-34 Opcional: atualização para Spring Boot 2.7.3
> - TAREFA: Validação e segurança

> [!summary]- 04 - Domínio e ORM, autorizações
> - 04-01 Visão geral do capítulo
> - 04-02 Visão geral do sistema DSLearn
> - 04-03 Baixando o projeto pronto (opcional)
> - 04-04 Setup do projeto DSLearn
> - 04-05 User, Role
> - 04-06 Course
> - 04-07 Offer
> - 04-08 Resource
> - 04-09 Section
> - 04-10 Enrollment, EnrollmentPK
> - 04-11 Enrollment seed
> - 04-12 Correção - Offer sem timezone
> - 04-13 Lesson, Content, Task
> - 04-14 Lesson seed, correção - lessonsDone
> - 04-15 Restante da implementação, clone do projeto
> - 04-16 Correções adicionais no código
> - 04-17 Últimas considerações sobre o projeto do Github
> - 04-18 Preparando para a segunda parte do capítulo - autorizações
> - 04-19 Criando os repositories
> - 04-20 Incluindo exceções, validação e segurança ao projeto
> - 04-21 Busca de usuário por id
> - 04-22 Autorização customizada em nível de serviço PARTE 1
> - 04-23 Autorização customizada em nível de serviço PARTE 2
> - 04-24 Conteúdo customizado para usuário logado
> - 04-25 Refresh token
> - 04-26 Pré-autorizando métodos por perfil de usuário
> - 04-27 Desafio para entregar
> - TAREFA: MovieFlix domínio e autorização

> [!summary]- 05 - Consultas ao banco de dados
> -05-01 Visão geral do capítulo
> - 05-02 Baixando os projetos prontos
> - 05-03 Orientações de estudo sobre SQL
> - 05-04 Postgresql 12 instalado neste momento
> - 05-05 URI 2602 - Elaborando a consulta
> - 05-06 Baixando os projetos iniciados dos estudos de caso
> - 05-07 URI 2602 Spring Boot SQL
> - 05-08 URI 2602 Spring Boot JPQL
> - 05-09 URI 2611 INNER JOIN Elaborando a consulta
> - 05-10 URI 2611 Spring Boot SQL e JPQL
> - 05-11 URI 2621 BETWEEN LIKE Elaborando a consulta
> - 05-12 URI 2621 Spring Boot SQL e JPQL
> - 05-13 Dica - pratique um pouco se você estiver precisando
> - 05-14 URI 2609 GROUP BY Elaborando a consulta
> - 05-15 URI 2609 Spring Boot SQL e JPQL
> - 05-16 URI 2737 UNION ALL Elaborando a consulta
> - 05-17 URI 2737 Solução alternativa
> - 05-18 URI 2737 Spring Boot SQL
> - 05-19 URI 2990 NOT IN Elaborando a consulta
> - 05-20 URI 2990 Solução alternativa com LEFT JOIN
> - 05-21 URI 2990 Spring Boot SQL e JPQL
> - 05-22 Preparando o DSCatalog do fim do capítulo 3
> - 05-23 Query methods
> - 05-24 Problema N+1 consultas com Spring Data JPA
> - 05-25 Disclaimer - avisos sobre o DSCatalog
> - 05-26 Filtrar produtos, INNER JOIN, IN
> - 05-27 Filtrar produtos, DISTINCT, IS NULL
> - 05-28 Filtrar produto, FNC, LIKE, LOWER, CONCAT, Trim
> - 05-29 Filtrar produtos, COALESCE, List
> - 05-30 Lidando com o famigerado problema N mais 1 consultas
> - 05-31 Corrigindo os testes do DSCatalog
> - 05-32 Configuração de CORS no DSCatalog
> - 05-33 Consulta de notificações do DSLearn
> - 05-34 Apresentando o desafio para entregar
> - 05-35 Explicação adicional: DTOs de cada requisição
> - TAREFA: MovieFlix casos de uso

> [!summary]- 06 - Docker, implantação, CI/CD
> - 06-01 Visão geral do capítulo
> - 06-02 Instalação do Docker
> - 06-03 Introdução a Docker e containers
> - 06-04 Imagem, container, registry
> - 06-05 Docker ps, images, pull, start, stop
> - 06-06 Instanciando um container Postgres
> - 06-07 Comandos básicos de manutenção no Docker
> - 06-08 Arquivo Dockerfile
> - 06-09 Analisando os demais exemplos de Dockerfile - AWS CLI, Spring Boot
> - 06-10 Volumes no Docker
> - 06-11 Enviando imagens para o DockerHub
> - 06-12 Começando a implantação manual - baixando o DSCatalog
> - 06-13 Perfis de projeto, variáveis de ambiente
> - 06-14 Gerando imagem com Dockerfile
> - 06-15 Criando base de dados Postgres remota no Heroku
> - 06-16 Instanciando um container no modo dev
> - 06-17 Cadastro na Amazon AWS e usuário IAM
> - 06-18 Criando instância EC2
> - 06-19 Acessar instância EC2 via SSH e instalar Docker
> - 06-20 Criando base de dados no Amazon RDS
> - 06-21 Conectando e instanciando a base de dados
> - 06-22 Enviando imagem para DockerHub
> - 06-23 Instanciando um container para conectar ao banco do RDS
> - 06-24 Instanciando o container no EC2
> - 06-25 CI CD no Heroku
> - 06-26 CI CD na AWS com Github Actions - visão geral
> - 06-27 Primeiro teste Github Actions
> - 06-28 Etapa 1 - Conexão e Cloud Shell
> - 06-29 Etapa 2 - Rede
> - 06-30 Etapa 3 - Banco de dados RDS
> - 06-31 Administração do banco de dados
> - 06-32 Etapa 4 - Aplicação Elastic Beanstalk e bucket S3
> - 06-33 Etapa 5 - Subindo build zero para nuvem
> - 06-34 Etapa 6 - Implantando build zero no Elastic Beanstalk
> - 06-35 Etapa 7 - Criando environment no Elastic Beanstalk
> - 06-36 Etapa 8 - Configurando variáveis de ambiente adicionais
> - 06-37 Etapa 9 - Configurando environment secrets no Github
> - 06-38 Etapa 10 - Incluindo pipeline Github Actions
> - 06-39 Exterminando os recursos da AWS
