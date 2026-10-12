---
title: Sql com python para iniciantes
description: "como criar estruturas, inserir e atualizar dados, cruzar informações entre tabelas e até integrar o SQL ao Python"
tags:
  - banco-de-dados
  - Python
---
Entrar no universo dos dados pode parecer desafiador no começo, mas há uma linguagem que abre portas para qualquer projeto: o SQL. Aqui, você vai descobrir como, com poucos comandos, é possível conversar diretamente com bancos de dados, extrair relatórios precisos e alimentar suas aplicações, seja um site, um app móvel ou até mesmo um pipeline de análise em Python.

Neste guia, reunimos tudo o que você precisa para partir do básico até consultas mais sofisticadas. Vamos mostrar como criar estruturas, inserir e atualizar dados, cruzar informações entre tabelas e até integrar o SQL ao Python para transformar resultados em gráficos e insights. Em cada etapa, você encontrará exemplos práticos e dicas para aplicar imediatamente no seu ambiente.

Prepare-se para transformar aquele amontoado de linhas e colunas em respostas claras às suas perguntas de negócio.

## O que é SQL?

SQL, sigla para **Structured Query Language**, é a linguagem usada para lidar com dados que estão organizados em tabelas, os chamados bancos de dados **relacionais**. Essas tabelas funcionam como planilhas, com linhas e colunas, só que com muito mais poder e estrutura por trás.

A grande força do SQL está na sua capacidade de **consultar, inserir, atualizar, excluir e organizar dados** com comandos simples, diretos e que se aproximam bastante da linguagem natural. Por isso, mesmo quem está começando na área de tecnologia consegue entender o básico sem se perder logo no início.

Desde sua criação nos anos 1970, o SQL se tornou o padrão mais utilizado no mundo para gerenciar bancos de dados. Está presente em sistemas pequenos, como aplicativos simples, até os gigantescos bancos de dados corporativos usados por empresas globais.

Ele é uma linguagem **declarativa**, o que significa que você não precisa dizer ao sistema *como* fazer algo, apenas informar *o que* deseja. Por exemplo, se você quiser saber todos os clientes de uma cidade específica, você pode escrever o comando certo, e o banco se encarrega de encontrar a resposta da forma mais eficiente possível.

Profissionais de diferentes áreas usam o SQL no dia a dia: analistas de dados, desenvolvedores, cientistas de dadose **administradores de banco**. Com ele, é possível extrair insights, integrar informações, manter a organização e até definir quem pode ou não acessar determinados dados.

Os comandos mais usados são:

- `SELECT ` para consultas;
- `INSERT ` para adicionar novos dados;
- `UPDATE ` para modificar informações existentes;
- `DELETE ` para remover registros;
- `CREATE`, `ALTER ` e `DROP ` para estruturar ou modificar as tabelas e bancos de dados em si.

### SQL é uma linguagem de programação?

Sim, o SQL é uma [linguagem de programação](https://hub.asimov.academy/blog/linguagem-de-programacao-o-que-e/), mas não é uma linguagem convencional. Chamamos de [**DSL (Domain-Specific Language)**](https://en.wikipedia.org/wiki/Domain-specific_language) ou linguagem de domínio específico, porque seu foco está inteiramente em **bancos de dados relacionais**. Enquanto linguagens como Python ou [**Java**](https://www.java.com/pt-BR/) servem para construir desde sites até jogos complexos, o SQL existe para fazer bem o que se propõe: **armazenar, consultar, atualizar e gerenciar dados**.

Uma das características que o diferencia é seu estilo **declarativo**. Em vez de instruir passo a passo como o sistema deve executar cada ação, você apenas define *o que* deseja, por exemplo, *“me traga todos os pedidos feitos em junho”* e deixa o banco de dados encontrar a melhor forma de entregar esse resultado. Isso simplifica muito a escrita de consultas e coloca a responsabilidade da otimização de desempenho para o próprio mecanismo do banco.

Por outro lado, essa especialização impede que o SQL seja usado sozinho para criar interfaces ou lógica de negócios mais complexa. Para isso, ele costuma ser combinado com linguagens de uso geral, que pegam os dados obtidos pelo SQL e os transformam em aplicações completas.

Portanto, o SQL não é uma linguagem de programação no sentido tradicional. Ele desempenha um papel importantíssimo na manipulação de dados.

## Para que serve o SQL?

SQL é a ferramenta que dá vida aos bancos de dados relacionais, oferecendo comandos claros para guardar, atualizar, apagar e recuperar informações de maneira organizada. Quando você digita uma consulta, está dizendo ao sistema exatamente quais dados quer ver, sem se preocupar com os detalhes de como essas instruções serão executadas por baixo dos panos.

O **SQL é a linguagem** que dá vida aos bancos de dados relacionais, fornecendo comandos diretos para:

- **Armazenar e recuperar**: guardar novos registros e trazer informações específicas com consultas precisas.
- **Atualizar e excluir**: modificar dados existentes ou removê‑los conforme a lógica de negócio.
- **Manter a integridade**: aplicar regras que evitam inconsistências, como chaves primárias e relacionamentos entre tabelas.

Ele aparece em ação em cenários muito distintos:

- **Big Data**: integrado a plataformas como [Hadoop](https://hadoop.apache.org/) e [Spark](https://spark.apache.org/) , o SQL ajuda a extrair padrões, agrupar resultados e detectar anomalias em conjuntos imensos de dados.
- **Aplicativos web e móveis**: alimenta perfis de usuários, histórico de transações e preferências, garantindo que cada clique ou compra fique registrado de forma segura.
- **Sistemas corporativos**: de e‑commerce e CRM a gestão hospitalar, financeira, educacional e de RH, o SQL organiza catálogos de produtos, prontuários médicos, relatórios financeiros e bancos de currículos.
- **Business Intelligence**: base dos relatórios e dashboards, ele agrega vendas, custos e métricas de marketing para apoiar decisões estratégicas.
- **Ambientes críticos**: em bancos, governos e setores que não admitem falhas, o SQL assegura operações atômicas, backups automáticos e rastreabilidade completa de cada transação.

Com essa versatilidade, o SQL se mantém indispensável em qualquer empresa ou projeto que dependa de dados organizados, confiáveis e prontos para gerar insights.

## Principais comandos SQL

O SQL organiza sua sintaxe em quatro grandes famílias de comandos, cada uma com um papel específico na criação, modificação, consulta e segurança dos dados. Abaixo, você encontra o que precisa conhecer para começar a trabalhar com qualquer banco de dados relacional.

### DDL (Data Definition Language)

Esses comandos cuidam da **estrutura** dos bancos de dados, criando, alterando ou removendo tabelas e outros objetos:**CREATE**: cria novas tabelas, índices ou visões.

```sql
CREATE TABLE clientes (
  id INT PRIMARY KEY,
  nome VARCHAR(100),
  email VARCHAR(100)
);
```

- Aqui criamos a tabela clientes com três colunas: id, nome e email.

**ALTER**: modifica tabelas já existentes.

```sql
ALTER TABLE clientes ADD telefone VARCHAR(15);
```

- Esse comando adiciona a coluna telefone à tabela clientes.

**`DROP`**: exclui completamente um objeto do banco.

```sql
DROP TABLE clientes;
```

- Com isso, a tabela clientes é removida junto com todos os seus dados.

### DML (Data Manipulation Language)

Quando o assunto é **inserir, atualizar ou excluir** registros dentro das tabelas, usamos os comandos DML:

**INSERT**: adiciona novas linhas.

```sql
INSERT INTO clientes (nome, email)
VALUES ('João', 'joao@example.com');
```

- Isso cria um registro para o cliente João.

**UPDATE**: altera dados já armazenados.

```sql
UPDATE clientes
SET email = 'joao.novo@example.com'
WHERE nome = 'João';
```

- Aqui, atualizamos o e‑mail do cliente cujo nome é João.

**DELETE**: remove registros específicos.

```sql
DELETE FROM clientes
WHERE nome = 'João';
```

- Dessa forma, apagamos o registro de João da tabela.

### DQL (Data Query Language)

Para **consultar** informações e extrair relatórios, o DQL oferece o comando:

**SELECT**: recupera colunas e linhas de uma ou mais tabelas.

```sql
SELECT id, nome, email
FROM clientes
WHERE email LIKE '%@example.com';
```

- Essa consulta retorna apenas os clientes cujo e‑mail termina com @example.com. Você pode usar \* para buscar todas as colunas ou combinar várias tabelas com JOIN para obter relatórios mais complexos.

### DCL (Data Control Language)

Em ambientes corporativos, controlar quem pode ver ou alterar dados é essencial. Para isso, existem:

**GRANT**: concede permissões a usuários ou roles.

```sql
GRANT SELECT, INSERT ON clientes TO usuario_exemplo;
```

- Com isso, usuario\_exemplo pode ler e adicionar registros na tabela clientes.

**REVOKE**: remove essas permissões.

```sql
REVOKE INSERT ON clientes FROM usuario_exemplo;
```

- Esse comando impede que usuario\_exemplo continue inserindo novos dados, mas mantém o direito de leitura.

## O que são JOINS em SQL?

Em SQL, **[JOIN](https://hub.asimov.academy/blog/sql-join/)** é a ferramenta que permite reunir informações espalhadas em diferentes tabelas e apresentar tudo de uma vez só. Em vez de repetir dados em várias tabelas, você armazena cada informação apenas uma vez — por exemplo, detalhes de clientes em uma tabela, produtos em outra e pedidos em uma terceira e depois usa JOINs para juntar esses pedaços conforme a necessidade.

Quando usar um JOIN?

- **Reduzir redundância**: em vez de gravar o nome do cliente em cada pedido, você salva esse dado uma única vez e referencia por um ID.
- **Fazer consultas completas**: com um único SELECT, fica fácil filtrar, ordenar e calcular valores que envolvem várias tabelas, como “quais produtos a cliente Maria comprou em janeiro” ou “quais funcionários nunca receberam um bônus”.

### Principais tipos de JOIN

- **INNER JOIN** Retorna apenas as linhas que têm correspondência em ambas as tabelas. É a interseção: “mostre apenas quem fez ao menos um pedido”.
- **LEFT JOIN** Inclui todas as linhas da tabela à esquerda e, quando não existir correspondência na tabela à direita, preenche com NULL. Útil para listar todos os clientes, mesmo aqueles que ainda não compraram nada.
- **RIGHT JOIN** O inverso do LEFT JOIN: traz todas as linhas da tabela à direita e usa NULL quando não houver par na tabela à esquerda.
- **FULL OUTER JOIN** Combina LEFT e RIGHT JOIN, exibindo todas as linhas de ambas as tabelas e preenchendo com NULL onde não houver correspondência. Serve para ver quem comprou e quem não comprou, em um único resultado.
- **CROSS JOIN** Retorna o produto cartesiano das tabelas, ou seja, todas as combinações possíveis de linhas das duas tabelas. Raramente usado em produção, mas pode ser útil para gerar matrizes de teste ou preencher combinações de dados.

## Diferenças entre SQL e NoSQL

Os bancos de dados SQL e [NoSQL](https://pt.wikipedia.org/wiki/NoSQL) atendem a propósitos distintos, e entender suas características ajuda a optar pela solução certa.

Em um **banco relacional (SQL)**, os dados vivem em tabelas bem definidas, com linhas e colunas que seguem um **esquema rígido**. Antes de inserir qualquer informação, você precisa criar as tabelas e definir tipos de dados, por exemplo, que a coluna “idade” seja sempre um número inteiro. Isso garante **integridade** e **transações seguras** (propriedades ACID: atomicidade, consistência, isolamento e durabilidade), essenciais para sistemas bancários ou de reservas aéreas, onde cada operação precisa ser confiável e imediata.

Já um **banco não relacional (NoSQL)** adota um modelo **sem esquema fixo**, permitindo guardar documentos JSON, pares chave‑valor, grafos ou colunas largas. Essa flexibilidade faz com que alterações no formato dos dados como incluir novos campos ou trabalhar com estruturas variadas sejam operações simples. Para escalar, em vez de “turbinar” um único servidor, você distribui a carga entre vários nós, suportando **altos volumes de tráfego e dados** sem comprometer a disponibilidade.

No quesito **consistência**, o SQL opta por uma visão imediata dos dados assim que você grava algo, qualquer outra consulta vê a informação nova. Em contrapartida, muitos bancos NoSQL privilegiam a **consistência eventual**, onde diferentes réplicas podem demorar um pouco para convergir, mas em compensação garantem que a aplicação continue funcionando mesmo se parte do sistema ficar indisponível.

Para consultar informações, o SQL usa sua linguagem declarativa padrão, a **Structured Query Language**, que é uniforme entre diferentes fornecedores. No mundo NoSQL, você depende de [**APIs**](https://hub.asimov.academy/blog/api-python/) **ou linguagens específicas** de acordo com o tipo de banco escolhido, o que pode exigir um aprendizado adicional, mas também permite otimizações específicas para cada caso.

### Exemplo prático: Análise de dados com SQL e Python

Uma das combinações mais interessantes para quem trabalha com dados é unir a flexibilidade do Python com a agilidade das consultas SQL. A biblioteca `sqlite3`, que já vem inclusa na instalação padrão do Python, nos permite criar e acessar bancos de dados SQLite de forma simples, sem precisar instalar nada além do próprio Python.

No exemplo abaixo, vamos conectar a um arquivo de banco de dados chamado meu\_banco\_de\_dados.db, buscar todos os registros de uma tabela clientes e exibir cada linha no console:

```python
import sqlite3

# 1. Conexão ao banco de dados
conn = sqlite3.connect('meu_banco_de_dados.db')
cursor = conn.cursor()

# 2. Consulta SQL para obter todos os clientes
query = "SELECT id, nome, email, telefone FROM clientes"
cursor.execute(query)

# 3. Recupera os resultados e processa cada linha
resultados = cursor.fetchall()
for id_, nome, email, telefone in resultados:
    print(f"ID: {id_}  |  Nome: {nome}  |  E‑mail: {email}  |  Telefone: {telefone}")

# 4. Fechamento da conexão
conn.close()
```

### Passo a passo de como colocar em prática:

1. **Criar o banco de dados e a tabela (opcional)** Se ainda não tiver o arquivo, você pode criá-lo no próprio Python:

```python
import sqlite3

conn = sqlite3.connect('meu_banco_de_dados.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT
    );
''')
conn.commit()
conn.close()
```

2. **Inserir alguns registros**Para ter dados de exemplo, insira clientes:

```python
conn = sqlite3.connect('meu_banco_de_dados.db')
cursor = conn.cursor()

clientes_exemplo = [
    ("Ana Silva", "ana.silva@example.com", "11 99999-0001"),
    ("Bruno Souza", "bruno.souza@example.com", "11 99999-0002"),
    ("Carla Pereira", "carla.pereira@example.com", "11 99999-0003")
]

cursor.executemany(
    "INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)",
    clientes_exemplo
)
conn.commit()
conn.close()
```

3. **Executar a consulta e analisar os resultados  
  - **No exemplo principal, a consulta SELECT id, nome, email, telefone FROM clientes traz todas as colunas definidas. Você pode adaptar essa query para filtrar apenas nomes que contenham “Silva”:

```python
cursor.execute("SELECT * FROM clientes WHERE nome LIKE '%Silva%'")
```

4. **Ir além do console: usar Pandas para análise  
  - **Se quiser manipular ou visualizar esses dados de maneira mais avançada, basta integrar o sqlite3 com o **Pandas**:

```python
import pandas as pd
import sqlite3

conn = sqlite3.connect('meu_banco_de_dados.db')
df = pd.read_sql_query("SELECT * FROM clientes", conn)
conn.close()
# Exiba as primeiras linhas e algumas estatísticas simples
print(df.head())
print(df.describe(include='all'))
```

Assim, em poucos minutos você monta um fluxo completo de **criação**, **inserção**, **consulta** e **análise** de dados, deixando seu projeto pronto para relatórios, visualizações ou integrações com outras partes da aplicação.

## Referências

- [SQL Online IDE - Fast SQL Editor \| SQL Compiler](https://sqliteonline.com/)
- [Guia rápido de comandos SQLite3 por Regis da Silva // #PythonClub //](https://pythonclub.com.br/guia-rapido-comandos-sqlite3.html)
- [Supabase - The Postgres Development Platform](https://supabase.com/)
