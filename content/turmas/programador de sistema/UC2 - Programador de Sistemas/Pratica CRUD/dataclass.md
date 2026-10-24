---
description: "Uso de decorador @dataclass"
tags:
  - pratica
  - python
  - decorador
  - crud
  - didatica
  - programacao
---

## Conceitos iniciais

O **`@dataclass`** é um *decorator* (decorador) introduzido no Python 3.7 no módulo nativo `dataclasses`. Ele foi projetado para **simplificar a criação de classes cujo objetivo principal é armazenar dados** (como os modelos de entidade `Cliente`, `Produto` e `Pedido` usados na arquitetura POO).

---

### **1. Qual Problema Ele Resolve?**

Na Programação Orientada a Objetos tradicional em Python, criar uma classe simples para armazenar dados exige escrever muito código repetitivo (*boilerplate*), como o construtor `__init__`, a representação textual `__repr__` e os métodos de comparação `__eq__`.

#### **Sem `@dataclass` (POO Tradicional):**

```python
class Cliente:
    def __init__(self, id: int, nome: str, email: str):
        self.id = id
        self.nome = nome
        self.email = email

    # Necessário para exibir o objeto de forma legível no print()
    def __repr__(self):
        return f"Cliente(id={self.id}, nome='{self.nome}', email='{self.email}')"

    # Necessário para comparar se dois objetos possuem os mesmos valores
    def __eq__(self, other):
        if not isinstance(other, Cliente):
            return False
        return (self.id, self.nome, self.email) == (other.id, other.nome, other.email)
```

---

### **2. Como Funciona com `@dataclass`**

Ao adicionar o decorador `@dataclass` acima da classe e indicar os tipos dos atributos (*type hints*), o Python gera **automaticamente** em tempo de execução os métodos `__init__`, `__repr__`, `__eq__` e outros.

#### **Com `@dataclass`:**

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class Cliente:
    id: Optional[int]
    nome: str
    email: str
```

O código acima equivale exatamente a todas as linhas do exemplo tradicional sem `@dataclass`.

---

### **3. Principais Métodos Gerados Automaticamente**

1. **`__init__()` (Construtor)**: Analisa os atributos anotados na classe e cria os parâmetros do construtor na ordem em que foram declarados.
2. **`__repr__()` (Representação Amigável)**: Permite que o comando `print(cliente)` exiba uma string legível como `Cliente(id=1, nome='Ana', email='ana@email.com')`, útil para depuração.
3. **`__eq__()` (Comparação de Conteúdo)**: Compara dois objetos com base em seus valores internos (`c1 == c2`), e não no endereço de memória onde estão alocados.

---

### **4. Recursos Adicionais Úteis**

- **Objetos Imutáveis (`frozen=True`)**: Se você quiser criar uma classe cujos atributos não possam ser alterados após a criação (semelhante a uma tupla), passe `frozen=True`:

  ```python
  @dataclass(frozen=True)
  class Ponto:
      x: float
      y: float

  p = Ponto(10.0, 20.0)
  # p.x = 15.0  --> Lança um TypeError (dataclass congelada)
  ```

- **Valores Padrão**: Você pode atribuir valores padrão diretamente na declaração dos atributos:

  ```python
  @dataclass
  class Produto:
      nome: str
      preco: float
      estoque: int = 0  # Valor padrão
  ```

- **Combinação com Propriedades (`@property`)**: É possível adicionar métodos e propriedades calculadas normalmente dentro da dataclass, como o cálculo do valor total de um pedido:

  ```python
  @dataclass
  class Pedido:
      quantidade: int
      preco_unitario: float

      @property
      def valor_total(self) -> float:
          return self.quantidade * self.preco_unitario
  ```

---

💡 Quer ver como usar o método **`asdict()`** do módulo `dataclasses` para converter uma instância de `@dataclass` diretamente em um dicionário Python?

## Convertendo uma classe em dicionário com `asdict()`

A função **`asdict()`** do módulo `dataclasses` converte recursivamente uma instância de `@dataclass` (e quaisquer outras dataclasses aninhadas dentro dela) em um **dicionário nativo do Python** (`dict`).

---

### **1. Exemplo Prático de Uso**

```python
from dataclasses import dataclass, asdict
from typing import List, Optional

@dataclass
class Cliente:
    id: Optional[int]
    nome: str
    email: str

@dataclass
class Produto:
    id: Optional[int]
    nome: str
    preco: float

@dataclass
class Pedido:
    id: Optional[int]
    cliente: Cliente
    itens: List[Produto]

# 1. Instanciando os objetos
cliente_ana = Cliente(id=1, nome="Ana Silva", email="ana@email.com")
prod1 = Produto(id=101, nome="Notebook", preco=4500.0)
prod2 = Produto(id=202, nome="Mouse", preco=120.0)

pedido = Pedido(id=50, cliente=cliente_ana, itens=[prod1, prod2])

# 2. Convertendo a instância completa em dicionário
pedido_dict = asdict(pedido)

# Exibindo o resultado
print("Tipo retornado:", type(pedido_dict))
print(pedido_dict)
```

#### **Saída Gerada:**

```python
Tipo retornado: <class 'dict'>
{
    'id': 50,
    'cliente': {
        'id': 1,
        'nome': 'Ana Silva',
        'email': 'ana@email.com'
    },
    'itens': [
        {'id': 101, 'nome': 'Notebook', 'preco': 4500.0},
        {'id': 202, 'nome': 'Mouse', 'preco': 120.0}
    ]
}
```

Note como a conversão é **recursiva**: tanto o objeto `Cliente` interno quanto a lista de `Produto` foram convertidos automaticamente em dicionários e listas de dicionários.

---

### **2. Onde o `asdict()` facilita a vida no projeto?**

#### **a) Inserção Direta no SQLite com Marcadores Nomeados (`:chave`)**

Em vez de passar tuplas e contar posições `(cliente.nome, cliente.email)`, você pode usar os nomes dos campos diretamente nas queries do SQLite:

```python
import sqlite3

cliente = Cliente(id=None, nome="Carlos Souza", email="carlos@email.com")

conn = sqlite3.connect('meu_banco_de_dados.db')
cursor = conn.cursor()

# O SQLite aceita um dicionário quando se usa a sintaxe :nome_do_campo
cursor.execute(
    "INSERT INTO clientes (nome, email) VALUES (:nome, :email);",
    asdict(cliente)
)
conn.commit()
conn.close()
```

#### **b) Retorno de APIs JSON no Bottle**

O framework Bottle converte dicionários retornados pelas rotas automaticamente em respostas no formato `JSON`:

```python
from bottle import get, template
from dataclasses import asdict

@get('/api/clientes/<id:int>')
def obter_cliente_api(id: int):
    cliente = cliente_dao.buscar_por_id(id)
    if not cliente:
        return {"erro": "Cliente não encontrado"}
    
    # O Bottle envia como JSON (Content-Type: application/json)
    return asdict(cliente)
```

---

💡 Quer ver o caminho inverso, ou seja, como usar desempacotamento de dicionário (`**dados`) para reconstruir um objeto `@dataclass` a partir de uma linha vinda do banco de dados?

## Caminho inverso com `asdict()`

O caminho inverso — reconstruir um objeto `@dataclass` a partir de um registro lido do banco de dados — é realizado combinando a funcionalidade **`row_factory = sqlite3.Row`** com o **desempacotamento de dicionário (`**dados`)**.

---

### **Como Funciona o Fluxo**

1. **`sqlite3.Row`**: Quando configurado na conexão, transforma as linhas retornadas pelo cursor em objetos que mapeiam os nomes das colunas aos seus respectivos valores.
2. **`dict(row)`**: Converte a linha `sqlite3.Row` em um dicionário nativo do Python (onde as chaves correspondem exatamente aos nomes das colunas no `SELECT`).
3. **`**dados` (Unpacking)**: Desempacota o dicionário passando cada par `chave=valor` como argumento nomeado para o construtor `__init__` gerado pela `@dataclass`.

---

### **Exemplo Prático Passo a Passo**

#### **1. Definição da Dataclass**

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class Cliente:
    id: Optional[int]
    nome: str
    email: str
```

#### **2. Reconstruindo um Registro Único (`fetchone`)**

```python
import sqlite3

conn = sqlite3.connect('meu_banco_de_dados.db')
# Habilita o acesso às colunas por nome e a conversão para dict
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# Executa a consulta
cursor.execute("SELECT id, nome, email FROM clientes WHERE id = ?;", (1,))
row = cursor.fetchone()

if row:
    # dict(row) converte o Row para: {'id': 1, 'nome': 'Ana Silva', 'email': 'ana@email.com'}
    dados_dict = dict(row)

    # O ** desempacota o dicionário como: Cliente(id=1, nome='Ana Silva', email='ana@email.com')
    cliente = Cliente(**dados_dict)

    print("Tipo do Objeto:", type(cliente))  # <class '__main__.Cliente'>
    print("Dados do Cliente:", cliente.nome, cliente.email)

conn.close()
```

---

#### **3. Reconstruindo Múltiplos Registros (`fetchall`)**

Para mapear toda uma tabela diretamente em uma lista de objetos `@dataclass`, pode-se utilizar uma *list comprehension*:

```python
cursor.execute("SELECT id, nome, email FROM clientes ORDER BY id DESC;")
rows = cursor.fetchall()

# Converte cada linha retornada em uma instância da dataclass Cliente
lista_clientes = [Cliente(**dict(row)) for row in rows]

for c in lista_clientes:
    print(f"Cliente #{c.id}: {c.nome} ({c.email})")
```

---

### **⚠️ Cuidados e Boas Práticas**

- **Correspondência exata de nomes**: As chaves do dicionário gerado pelo `SELECT` devem ter exatamente os mesmos nomes dos atributos da `@dataclass`. Se a coluna no banco tiver um nome diferente, utilize alias (`AS`) no SQL:

  ```sql
  SELECT id, nome_cliente AS nome, email_contato AS email FROM clientes;
  ```

- **Colunas extras na consulta**: Se a instrução `SELECT *` retornar colunas que não foram declaradas como atributos na `@dataclass`, o desempacotamento `**dados` lançará um erro `TypeError: __init__() got an unexpected keyword argument`. Para evitar isso, explicite as colunas desejadas no `SELECT` ou crie uma função utilitária para filtrar apenas as chaves aceitas pela classe:

```python
import inspect

def instanciar_dataclass_segura(cls, dados_dict: dict):
    """Instancia uma dataclass ignorando colunas extras retornadas pelo banco."""
    atributos_validos = inspect.signature(cls).parameters.keys()
    dados_filtrados = {k: v for k, v in dados_dict.items() if k in atributos_validos}
    return cls(**dados_filtrados)
```

---

💡 Quer ver como implementar uma camada de **Data Mapper / Repositório Genérico** em Python para automatizar esse processo de ida e volta do banco de dados para qualquer `@dataclass`?

## Uso avançado com mapeamento de dados

A implementação de um **Repositório Genérico (Data Mapper)** em Python permite automatizar completamente o ciclo de **persistência e reconstrução** de dados.

Utilizando a metaclasse de genéricos do Python (`typing.Generic`), a introspecção das `@dataclass` (`dataclasses.fields`) e as funções `asdict()` e `**dados` (unpacking), é possível criar **uma única classe repositório** capaz de realizar o CRUD básico (`salvar`, `buscar_por_id`, `listar_todos` e `deletar`) para qualquer entidade do sistema sem duplicação de código SQL.

---

### **1. Como Funciona a Lógica Interna**

1. **Introspecção dos Campos**: A função `dataclasses.fields(model_cls)` descobre em tempo de execução quais são as colunas da tabela a partir dos atributos declarados na `@dataclass`.
2. **Geração Dinâmica de SQL**: Com os nomes dos campos em mãos, o repositório monta os comandos `INSERT`, `UPDATE`, `SELECT` e `DELETE` dinamicamente.
3. **Mapeamento de Entrada (`asdict`)**: Ao salvar, a `@dataclass` é convertida para dicionário com `asdict(entidade)` e enviada ao SQLite com parâmetros nomeados (`:campo`).
4. **Mapeamento de Saída (`**dados`)**: Ao ler do banco, o `sqlite3.Row` é convertido em dicionário e desempacotado no construtor da `@dataclass` (`T(**dados)`).

---

### **2. Implementação do `RepositorioGenerico[T]`**

Crie o módulo `dao/repositorio_generico.py`:

```python
import sqlite3
import inspect
from dataclasses import fields, asdict
from typing import TypeVar, Generic, List, Optional, Type
from database import DatabaseManager

# TypeVar genérico que representará qualquer modelo @dataclass
T = TypeVar('T')

class RepositorioGenerico(Generic[T]):
    """
    Repositório genérico para operações CRUD em tabelas mapeadas para @dataclasses.
    """
    def __init__(self, db_mgr: DatabaseManager, model_cls: Type[T], tabela: str):
        self.db_mgr = db_mgr
        self.model_cls = model_cls
        self.tabela = tabela
        
        # Descobre os nomes das colunas declaradas na @dataclass via introspecção
        self.colunas = [f.name for f in fields(model_cls)]
        # Separa a chave primária 'id' das demais colunas para instruções de escrita
        self.colunas_sem_id = [col for col in self.colunas if col != 'id']

    def _mapear_row(self, row: sqlite3.Row) -> T:
        """Converte uma linha sqlite3.Row em uma instância da @dataclass T."""
        dados = dict(row)
        # Filtra apenas parâmetros aceitos pela dataclass para evitar exceções
        atributos_validos = inspect.signature(self.model_cls).parameters.keys()
        dados_filtrados = {k: v for k, v in dados.items() if k in atributos_validos}
        return self.model_cls(**dados_filtrados)

    def buscar_por_id(self, id: int) -> Optional[T]:
        """Busca um registro pelo ID e reconstrói o objeto @dataclass."""
        sql = f"SELECT * FROM {self.tabela} WHERE id = ?;"
        with self.db_mgr.get_connection() as conn:
            row = conn.execute(sql, (id,)).fetchone()
            return self._mapear_row(row) if row else None

    def listar_todos(self) -> List[T]:
        """Retorna todos os registros da tabela convertidos em objetos @dataclass."""
        sql = f"SELECT * FROM {self.tabela} ORDER BY id DESC;"
        with self.db_mgr.get_connection() as conn:
            rows = conn.execute(sql).fetchall()
            return [self._mapear_row(r) for r in rows]

    def salvar(self, entidade: T) -> T:
        """Insere um novo registro ou atualiza um existente com base na presença do atributo 'id'."""
        dados = asdict(entidade)
        entidade_id = getattr(entidade, 'id', None)

        with self.db_mgr.get_connection() as conn:
            if entidade_id:
                # Monta a cláusula SET dinâmica: UPDATE tabela SET col1 = :col1, col2 = :col2 WHERE id = :id
                set_clause = ", ".join([f"{col} = :{col}" for col in self.colunas_sem_id])
                sql = f"UPDATE {self.tabela} SET {set_clause} WHERE id = :id;"
                conn.execute(sql, dados)
            else:
                # Monta a instrução INSERT dinâmica: INSERT INTO tabela (col1, col2) VALUES (:col1, :col2)
                cols = ", ".join(self.colunas_sem_id)
                vals = ", ".join([f":{col}" for col in self.colunas_sem_id])
                sql = f"INSERT INTO {self.tabela} ({cols}) VALUES ({vals});"
                cursor = conn.execute(sql, dados)
                
                # Atualiza o ID atribuído pelo banco na própria instância em memória
                if hasattr(entidade, 'id'):
                    setattr(entidade, 'id', cursor.lastrowid)

        return entidade

    def deletar(self, id: int) -> None:
        """Remove um registro do banco pelo ID."""
        sql = f"DELETE FROM {self.tabela} WHERE id = ?;"
        with self.db_mgr.get_connection() as conn:
            conn.execute(sql, (id,))
```

---

### **3. Como Utilizar na Prática**

#### **Uso Direto (Zero Código Duplicado)**

Para entidades com operações simples de CRUD (como `Cliente` e `Produto`), não é necessário criar classes de DAO manualmente:

```python
from database import DatabaseManager
from models import Cliente, Produto
from dao.repositorio_generico import RepositorioGenerico

db_mgr = DatabaseManager()

# Instancia repositórios genéricos tipados
cliente_repo = RepositorioGenerico[Cliente](db_mgr, Cliente, "clientes")
produto_repo = RepositorioGenerico[Produto](db_mgr, Produto, "produtos")

# 1. Inserir Cliente
novo_cliente = Cliente(id=None, nome="Lucas Mendes", email="lucas@email.com")
cliente_repo.salvar(novo_cliente)
print("Cliente cadastrado com ID:", novo_cliente.id)

# 2. Listar todos
clientes = cliente_repo.listar_todos()  # Retorna List[Cliente]

# 3. Buscar e Atualizar
cliente = cliente_repo.buscar_por_id(1)
if cliente:
    cliente.nome = "Lucas Mendes Alterado"
    cliente_repo.salvar(cliente)  # Executa UPDATE automaticamente
```

---

#### **Herança para Consultas Especializadas**

Quando uma entidade exigir consultas personalizadas com `JOIN` ou regras transacionais específicas (como a criação de `Pedidos`), você estende o `RepositorioGenerico`:

```python
from dao.repositorio_generico import RepositorioGenerico
from models import Pedido
from typing import List

class PedidoRepositorio(RepositorioGenerico[Pedido]):
    """Herda o CRUD básico do RepositorioGenerico e adiciona consultas com JOIN."""
    def __init__(self, db_mgr):
        super().__init__(db_mgr, Pedido, "pedidos")

    def listar_com_detalhes(self) -> List[Pedido]:
        query = """
            SELECT p.id, p.cliente_id, p.produto_id, p.quantidade, p.preco_unitario, p.data_pedido,
                   c.nome AS cliente_nome, prod.nome AS produto_nome
            FROM pedidos p
            INNER JOIN clientes c ON p.cliente_id = c.id
            INNER JOIN produtos prod ON p.produto_id = prod.id
            ORDER BY p.id DESC;
        """
        with self.db_mgr.get_connection() as conn:
            cursor = conn.execute(query)
            return [self._mapear_row(r) for r in cursor.fetchall()]
```

---

### **Benefícios da Abordagem**

- **Redução Drástica de Boilerplate**: Não é necessário escrever consultas SQL `INSERT` ou `UPDATE` repetitivas para cada tabela do sistema.
- **Segurança**: Todas as consultas utilizam parametrização por dicionário (`:campo`), prevenindo injeções de SQL.
- **Manutenibilidade**: Ao adicionar um novo campo na `@dataclass` e na tabela, a persistência é atualizada automaticamente.
