---
description: "Exemplo prático de POO de um cadastro com Python e banco de dados Sqlite."
tags:
  - pratica
  - python
  - sqlite
  - crud
  - didatica
  - programacao
---

Usando [[dataclass]]

## Refatorando o app com programação orientada a objetos

Para reestruturar o arquivo `app.py` utilizando o paradigma de **Programação Orientada a Objetos (POO)**, aplicamos o padrão de arquitetura em camadas:

1. **Classes de Modelo / Domínio (`Cliente`, `Produto`, `Pedido`)**: Representam as entidades do negócio com seus atributos e métodos.
2. **Classes DAO / Repositório (`ClienteDAO`, `ProdutoDAO`, `PedidoDAO`)**: Encapsulam a lógica de acesso ao banco de dados SQLite, executando comandos DDL/DML, garantindo a parametrização segura (`?`) e o controle transacional (`commit()` / `rollback()`).
3. **Controlador Web (Rotas do Bottle)**: Recebe as requisições do navegador, interage com as classes de modelo e DAO e retorna as views renderizadas.

---

### **Código Completo do `app.py` em POO**

```python
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional
from bottle import get, post, request, redirect, template, run

DB_PATH = Path(__file__).with_name("meu_banco_de_dados.db")

# ==========================================
# 1. CAMADA DE DOMÍNIO / MODELOS (CLASSES)
# ==========================================

@dataclass
class Cliente:
    """Representa a entidade Cliente."""
    id: Optional[int]
    nome: str
    email: str

@dataclass
class Produto:
    """Representa a entidade Produto."""
    id: Optional[int]
    nome: str
    preco: float
    estoque: int

@dataclass
class Pedido:
    """Representa a entidade Pedido."""
    id: Optional[int]
    cliente_id: int
    produto_id: int
    quantidade: int
    preco_unitario: float
    cliente_nome: Optional[str] = None
    produto_nome: Optional[str] = None
    data_pedido: Optional[str] = None

    @property
    def valor_total(self) -> float:
        """Cálculo automático do valor total do pedido."""
        return self.quantidade * self.preco_unitario

# ==========================================
# 2. CAMADA DE BANCO DE DADOS (GERENCIADOR DE CONEXÃO)
# ==========================================

class DatabaseManager:
    """Gerencia conexões e inicialização das tabelas no SQLite."""
    def __init__(self, db_path: Path):
        self.db_path = db_path

    def get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        # Garante a integridade referencial das Chaves Estrangeiras (FK)
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn

    def inicializar_tabelas(self) -> None:
        """Executa scripts DDL para criação das tabelas se não existirem."""
        with self.get_connection() as conn:
            conn.executescript('''
                CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE
                );

                CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    preco REAL NOT NULL CHECK(preco >= 0.0),
                    estoque INTEGER NOT NULL DEFAULT 0 CHECK(estoque >= 0)
                );

                CREATE TABLE IF NOT EXISTS pedidos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cliente_id INTEGER NOT NULL,
                    produto_id INTEGER NOT NULL,
                    quantidade INTEGER NOT NULL CHECK(quantidade > 0),
                    preco_unitario REAL NOT NULL CHECK(preco_unitario >= 0.0),
                    data_pedido TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
                    FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE RESTRICT,
                    FOREIGN KEY (produto_id) REFERENCES produtos(id) ON DELETE RESTRICT
                );
            ''')

# ==========================================
# 3. CAMADA DE ACESSO A DADOS (DAOs)
# ==========================================

class ClienteDAO:
    """Operações CRUD para Clientes."""
    def __init__(self, db_mgr: DatabaseManager):
        self.db_mgr = db_mgr

    def listar_todos(self) -> List[Cliente]:
        with self.db_mgr.get_connection() as conn:
            cursor = conn.execute("SELECT id, nome, email FROM clientes ORDER BY id DESC;")
            return [Cliente(id=row['id'], nome=row['nome'], email=row['email']) for row in cursor.fetchall()]

    def buscar_por_id(self, cliente_id: int) -> Optional[Cliente]:
        with self.db_mgr.get_connection() as conn:
            row = conn.execute("SELECT id, nome, email FROM clientes WHERE id = ?;", (cliente_id,)).fetchone()
            return Cliente(id=row['id'], nome=row['nome'], email=row['email']) if row else None

    def salvar(self, cliente: Cliente) -> None:
        with self.db_mgr.get_connection() as conn:
            if cliente.id:
                conn.execute("UPDATE clientes SET nome = ?, email = ? WHERE id = ?;", 
                             (cliente.nome, cliente.email, cliente.id))
            else:
                conn.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", 
                             (cliente.nome, cliente.email))

    def deletar(self, cliente_id: int) -> None:
        with self.db_mgr.get_connection() as conn:
            conn.execute("DELETE FROM clientes WHERE id = ?;", (cliente_id,))

class ProdutoDAO:
    """Operações CRUD para Produtos."""
    def __init__(self, db_mgr: DatabaseManager):
        self.db_mgr = db_mgr

    def listar_todos(self) -> List[Produto]:
        with self.db_mgr.get_connection() as conn:
            cursor = conn.execute("SELECT id, nome, preco, estoque FROM produtos ORDER BY id DESC;")
            return [Produto(id=row['id'], nome=row['nome'], preco=row['preco'], estoque=row['estoque']) 
                    for row in cursor.fetchall()]

    def buscar_por_id(self, produto_id: int) -> Optional[Produto]:
        with self.db_mgr.get_connection() as conn:
            row = conn.execute("SELECT id, nome, preco, estoque FROM produtos WHERE id = ?;", (produto_id,)).fetchone()
            return Produto(id=row['id'], nome=row['nome'], preco=row['preco'], estoque=row['estoque']) if row else None

    def salvar(self, produto: Produto) -> None:
        with self.db_mgr.get_connection() as conn:
            if produto.id:
                conn.execute("UPDATE produtos SET nome = ?, preco = ?, estoque = ? WHERE id = ?;", 
                             (produto.nome, produto.preco, produto.estoque, produto.id))
            else:
                conn.execute("INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?);", 
                             (produto.nome, produto.preco, produto.estoque))

    def deletar(self, produto_id: int) -> None:
        with self.db_mgr.get_connection() as conn:
            conn.execute("DELETE FROM produtos WHERE id = ?;", (produto_id,))

class PedidoDAO:
    """Operações de Negócio e Transações para Pedidos."""
    def __init__(self, db_mgr: DatabaseManager):
        self.db_mgr = db_mgr

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
            return [
                Pedido(
                    id=row['id'],
                    cliente_id=row['cliente_id'],
                    produto_id=row['produto_id'],
                    quantidade=row['quantidade'],
                    preco_unitario=row['preco_unitario'],
                    cliente_nome=row['cliente_nome'],
                    produto_nome=row['produto_nome'],
                    data_pedido=row['data_pedido']
                ) for row in cursor.fetchall()
            ]

    def criar_pedido_transacional(self, cliente_id: int, produto_id: int, quantidade: int) -> None:
        """Garante baixa no estoque e registro do pedido em uma transação atômica."""
        conn = self.db_mgr.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("BEGIN IMMEDIATE;")

            # 1. Consulta o produto e verifica o estoque
            cursor.execute("SELECT preco, estoque FROM produtos WHERE id = ?;", (produto_id,))
            prod = cursor.fetchone()

            if not prod or prod['estoque'] < quantidade:
                raise ValueError("Estoque insuficiente ou produto inexistente.")

            preco_unitario = prod['preco']

            # 2. Insere o pedido congelando o preço unitário
            cursor.execute('''
                INSERT INTO pedidos (cliente_id, produto_id, quantidade, preco_unitario)
                VALUES (?, ?, ?, ?);
            ''', (cliente_id, produto_id, quantidade, preco_unitario))

            # 3. Baixa no estoque
            cursor.execute("UPDATE produtos SET estoque = estoque - ? WHERE id = ?;", 
                           (quantidade, produto_id))

            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()

# ==========================================
# 4. INSTANCIAÇÃO DOS SERVIÇOS
# ==========================================

db_manager = DatabaseManager(DB_PATH)
cliente_dao = ClienteDAO(db_manager)
produto_dao = ProdutoDAO(db_manager)
pedido_dao = PedidoDAO(db_manager)

# ==========================================
# 5. CONTROLADORES / ROTAS DO BOTTLE
# ==========================================

# --- ROTAS DE CLIENTES ---
@get('/')
def listar_clientes():
    msg_erro = request.query.get('erro', '')
    clientes = cliente_dao.listar_todos()
    return template('clientes', lista_clientes=clientes, msg_erro=msg_erro)

@post('/cadastrar')
def cadastrar_cliente():
    nome = (request.forms.getunicode('nome') or '').strip()
    email = (request.forms.getunicode('email') or '').strip()
    try:
        cliente_dao.salvar(Cliente(id=None, nome=nome, email=email))
        redirect('/')
    except sqlite3.IntegrityError:
        redirect('/?erro=E-mail+já+cadastrado.')

@get('/editar/<id:int>')
def exibir_edicao_cliente(id: int):
    cliente = cliente_dao.buscar_por_id(id)
    if not cliente:
        redirect('/?erro=Cliente+não+encontrado.')
    return template('cliente_editar', cliente=cliente)

@post('/editar/<id:int>')
def salvar_edicao_cliente(id: int):
    nome = (request.forms.getunicode('nome') or '').strip()
    email = (request.forms.getunicode('email') or '').strip()
    try:
        cliente_dao.salvar(Cliente(id=id, nome=nome, email=email))
        redirect('/')
    except sqlite3.IntegrityError:
        redirect('/?erro=E-mail+pertence+a+outro+cliente.')

@get('/deletar/<id:int>')
def deletar_cliente(id: int):
    try:
        cliente_dao.deletar(id)
    except sqlite3.Error:
        redirect('/?erro=Não+é+possível+excluir+cliente+com+pedidos.')
    redirect('/')

# --- ROTAS DE PRODUTOS ---
@get('/produtos')
def listar_produtos():
    msg_erro = request.query.get('erro', '')
    produtos = produto_dao.listar_todos()
    return template('produtos', lista_produtos=produtos, msg_erro=msg_erro)

@post('/produtos/cadastrar')
def cadastrar_produto():
    nome = (request.forms.getunicode('nome') or '').strip()
    try:
        preco = float(request.forms.get('preco', 0))
        estoque = int(request.forms.get('estoque', 0))
        produto_dao.salvar(Produto(id=None, nome=nome, preco=preco, estoque=estoque))
        redirect('/produtos')
    except Exception as e:
        redirect(f'/produtos?erro={e}')

@get('/produtos/editar/<id:int>')
def exibir_edicao_produto(id: int):
    produto = produto_dao.buscar_por_id(id)
    if not produto:
        redirect('/produtos?erro=Produto+não+encontrado.')
    return template('produto_editar', produto=produto)

@post('/produtos/editar/<id:int>')
def salvar_edicao_produto(id: int):
    nome = (request.forms.getunicode('nome') or '').strip()
    try:
        preco = float(request.forms.get('preco', 0))
        estoque = int(request.forms.get('estoque', 0))
        produto_dao.salvar(Produto(id=id, nome=nome, preco=preco, estoque=estoque))
        redirect('/produtos')
    except Exception as e:
        redirect(f'/produtos?erro={e}')

@get('/produtos/deletar/<id:int>')
def deletar_produto(id: int):
    try:
        produto_dao.deletar(id)
    except sqlite3.Error:
        redirect('/produtos?erro=Não+é+possível+excluir+produto+vinculado+a+pedidos.')
    redirect('/produtos')

# --- ROTAS DE PEDIDOS ---
@get('/pedidos')
def listar_pedidos():
    msg_erro = request.query.get('erro', '')
    clientes = cliente_dao.listar_todos()
    produtos = [p for p in produto_dao.listar_todos() if p.estoque > 0]
    pedidos = pedido_dao.listar_com_detalhes()
    return template('pedidos', lista_clientes=clientes, lista_produtos=produtos, lista_pedidos=pedidos, msg_erro=msg_erro)

@post('/pedidos/cadastrar')
def cadastrar_pedido():
    try:
        cliente_id = int(request.forms.get('cliente_id'))
        produto_id = int(request.forms.get('produto_id'))
        quantidade = int(request.forms.get('quantidade', 1))
        
        pedido_dao.criar_pedido_transacional(cliente_id, produto_id, quantidade)
        redirect('/pedidos')
    except Exception as e:
        redirect(f'/pedidos?erro={e}')

# ==========================================
# 6. INICIALIZAÇÃO DO SERVIDOR
# ==========================================
if __name__ == '__main__':
    db_manager.inicializar_tabelas()
    print("Servidor POO ativo em http://localhost:8080 ...")
    run(host='localhost', port=8080, debug=True, reloader=True)
```

---

### **Vantagens de Organizar com POO**

1. **Separação de Responsabilidades (SoC)**: O Bottle lida apenas com requisições HTTP e renderização dos templates (`.tpl`). As regras de negócio e cálculo de valores ficam encapsuladas nas classes de modelo (`Pedido.valor_total`), enquanto as consultas SQL pertencem exclusivamente aos DAOs.
2. **Encapsulamento de Transações**: A classe `PedidoDAO` contém o método `criar_pedido_transacional()` que executa o `BEGIN IMMEDIATE`, a verificação de estoque e a baixa automática com `commit()` e `rollback()` em um único local.
3. **Legibilidade e Tipagem**: A utilização de `@dataclass` e anotações de tipo (`typing`) torna o código mais limpo e imune a erros comuns de manipulação manual de dicionários ou tuplas brutas do banco de dados.

## Organizando o app em Módulos

Para modularizar a aplicação e aplicar as melhores práticas de **arquitetura de software**, separaremos o projeto em pacotes e arquivos específicos para cada responsabilidade.

---

### **Árvore de Diretórios e Arquivos do Projeto**

```text
meu_projeto/
│
├── app.py                      # Ponto de entrada (Main) e rotas HTTP do Bottle
├── database.py                 # Gerenciador de conexões e tabelas SQLite
│
├── models/                     # Pacote com as entidades de domínio
│   ├── __init__.py
│   ├── cliente.py
│   ├── produto.py
│   └── pedido.py
│
├── dao/                        # Pacote com a camada de persistência (DAOs)
│   ├── __init__.py
│   ├── cliente_dao.py
│   ├── produto_dao.py
│   └── pedido_dao.py
│
├── views/                      # Templates HTML do Bottle (SimpleTemplate)
│   ├── base.tpl
│   ├── clientes.tpl
│   ├── cliente_editar.tpl
│   ├── produtos.tpl
│   ├── produto_editar.tpl
│   └── pedidos.tpl
│
└── static/                     # Arquivos estáticos (CSS/JS)
    └── style.css
```

---

### **1. Módulos do Pacote `models/`**

#### **`models/cliente.py`**

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class Cliente:
    """Entidade que representa um Cliente do sistema."""
    id: Optional[int]
    nome: str
    email: str
```

#### **`models/produto.py`**

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class Produto:
    """Entidade que representa um Produto em estoque."""
    id: Optional[int]
    nome: str
    preco: float
    estoque: int
```

#### **`models/pedido.py`**

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class Pedido:
    """Entidade que representa uma Ordem de Compra/Pedido."""
    id: Optional[int]
    cliente_id: int
    produto_id: int
    quantidade: int
    preco_unitario: float
    cliente_nome: Optional[str] = None
    produto_nome: Optional[str] = None
    data_pedido: Optional[str] = None

    @property
    def valor_total(self) -> float:
        """Propriedade calculada dinamicamente."""
        return self.quantidade * self.preco_unitario
```

#### **`models/__init__.py`**

```python
from .cliente import Cliente
from .produto import Produto
from .pedido import Pedido

__all__ = ["Cliente", "Produto", "Pedido"]
```

---

### **2. Gerenciador de Banco de Dados (`database.py`)**

```python
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "meu_banco_de_dados.db"

class DatabaseManager:
    """Responsável por gerenciar conexões e inicialização das tabelas."""
    def __init__(self, db_path: Path = DB_PATH):
        self.db_path = db_path

    def get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        # Ativa a verificação de Foreign Keys no SQLite
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn

    def inicializar_tabelas(self) -> None:
        """Cria as tabelas caso ainda não existam."""
        with self.get_connection() as conn:
            conn.executescript('''
                CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE
                );

                CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    preco REAL NOT NULL CHECK(preco >= 0.0),
                    estoque INTEGER NOT NULL DEFAULT 0 CHECK(estoque >= 0)
                );

                CREATE TABLE IF NOT EXISTS pedidos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cliente_id INTEGER NOT NULL,
                    produto_id INTEGER NOT NULL,
                    quantidade INTEGER NOT NULL CHECK(quantidade > 0),
                    preco_unitario REAL NOT NULL CHECK(preco_unitario >= 0.0),
                    data_pedido TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
                    FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE RESTRICT,
                    FOREIGN KEY (produto_id) REFERENCES produtos(id) ON DELETE RESTRICT
                );
            ''')
```

---

### **3. Módulos do Pacote `dao/`**

#### **`dao/cliente_dao.py`**

```python
import sqlite3
from typing import List, Optional
from database import DatabaseManager
from models.cliente import Cliente

class ClienteDAO:
    """Data Access Object para a entidade Cliente."""
    def __init__(self, db_mgr: DatabaseManager):
        self.db_mgr = db_mgr

    def listar_todos(self) -> List[Cliente]:
        with self.db_mgr.get_connection() as conn:
            cursor = conn.execute("SELECT id, nome, email FROM clientes ORDER BY id DESC;")
            return [Cliente(id=r['id'], nome=r['nome'], email=r['email']) for r in cursor.fetchall()]

    def buscar_por_id(self, cliente_id: int) -> Optional[Cliente]:
        with self.db_mgr.get_connection() as conn:
            r = conn.execute("SELECT id, nome, email FROM clientes WHERE id = ?;", (cliente_id,)).fetchone()
            return Cliente(id=r['id'], nome=r['nome'], email=r['email']) if r else None

    def salvar(self, cliente: Cliente) -> None:
        with self.db_mgr.get_connection() as conn:
            if cliente.id:
                conn.execute("UPDATE clientes SET nome = ?, email = ? WHERE id = ?;", 
                             (cliente.nome, cliente.email, cliente.id))
            else:
                conn.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", 
                             (cliente.nome, cliente.email))

    def deletar(self, cliente_id: int) -> None:
        with self.db_mgr.get_connection() as conn:
            conn.execute("DELETE FROM clientes WHERE id = ?;", (cliente_id,))
```

#### **`dao/produto_dao.py`**

```python
import sqlite3
from typing import List, Optional
from database import DatabaseManager
from models.produto import Produto

class ProdutoDAO:
    """Data Access Object para a entidade Produto."""
    def __init__(self, db_mgr: DatabaseManager):
        self.db_mgr = db_mgr

    def listar_todos(self) -> List[Produto]:
        with self.db_mgr.get_connection() as conn:
            cursor = conn.execute("SELECT id, nome, preco, estoque FROM produtos ORDER BY id DESC;")
            return [Produto(id=r['id'], nome=r['nome'], preco=r['preco'], estoque=r['estoque']) for r in cursor.fetchall()]

    def buscar_por_id(self, produto_id: int) -> Optional[Produto]:
        with self.db_mgr.get_connection() as conn:
            r = conn.execute("SELECT id, nome, preco, estoque FROM produtos WHERE id = ?;", (produto_id,)).fetchone()
            return Produto(id=r['id'], nome=r['nome'], preco=r['preco'], estoque=r['estoque']) if r else None

    def salvar(self, produto: Produto) -> None:
        with self.db_mgr.get_connection() as conn:
            if produto.id:
                conn.execute("UPDATE produtos SET nome = ?, preco = ?, estoque = ? WHERE id = ?;", 
                             (produto.nome, produto.preco, produto.estoque, produto.id))
            else:
                conn.execute("INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?);", 
                             (produto.nome, produto.preco, produto.estoque))

    def deletar(self, produto_id: int) -> None:
        with self.db_mgr.get_connection() as conn:
            conn.execute("DELETE FROM produtos WHERE id = ?;", (produto_id,))
```

#### **`dao/pedido_dao.py`**

```python
import sqlite3
from typing import List
from database import DatabaseManager
from models.pedido import Pedido

class PedidoDAO:
    """Data Access Object para a entidade Pedido."""
    def __init__(self, db_mgr: DatabaseManager):
        self.db_mgr = db_mgr

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
            return [
                Pedido(
                    id=r['id'], cliente_id=r['cliente_id'], produto_id=r['produto_id'],
                    quantidade=r['quantidade'], preco_unitario=r['preco_unitario'],
                    cliente_nome=r['cliente_nome'], produto_nome=r['produto_nome'],
                    data_pedido=r['data_pedido']
                ) for r in cursor.fetchall()
            ]

    def criar_pedido_transacional(self, cliente_id: int, produto_id: int, quantidade: int) -> None:
        """Cria o pedido e atualiza o estoque dentro de uma transação atômica."""
        conn = self.db_mgr.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("BEGIN IMMEDIATE;")

            cursor.execute("SELECT preco, estoque FROM produtos WHERE id = ?;", (produto_id,))
            prod = cursor.fetchone()

            if not prod or prod['estoque'] < quantidade:
                raise ValueError("Estoque insuficiente ou produto inexistente.")

            preco_unitario = prod['preco']

            cursor.execute('''
                INSERT INTO pedidos (cliente_id, produto_id, quantidade, preco_unitario)
                VALUES (?, ?, ?, ?);
            ''', (cliente_id, produto_id, quantidade, preco_unitario))

            cursor.execute("UPDATE produtos SET estoque = estoque - ? WHERE id = ?;", 
                           (quantidade, produto_id))

            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()
```

#### **`dao/__init__.py`**

```python
from .cliente_dao import ClienteDAO
from .produto_dao import ProdutoDAO
from .pedido_dao import PedidoDAO

__all__ = ["ClienteDAO", "ProdutoDAO", "PedidoDAO"]
```

---

### **4. Arquivo Principal (`app.py`)**

O arquivo `app.py` atua como o **orquestrador**, importando os módulos, configurando as instâncias e definindo as rotas web do Bottle:

```python
import sqlite3
from bottle import get, post, request, redirect, template, run

from database import DatabaseManager
from models import Cliente, Produto
from dao import ClienteDAO, ProdutoDAO, PedidoDAO

# Inicialização da infraestrutura e dos DAOs
db_mgr = DatabaseManager()
cliente_dao = ClienteDAO(db_mgr)
produto_dao = ProdutoDAO(db_mgr)
pedido_dao = PedidoDAO(db_mgr)

# --- ROTAS DE CLIENTES ---
@get('/')
def listar_clientes():
    msg_erro = request.query.get('erro', '')
    return template('clientes', lista_clientes=cliente_dao.listar_todos(), msg_erro=msg_erro)

@post('/cadastrar')
def cadastrar_cliente():
    nome = (request.forms.getunicode('nome') or '').strip()
    email = (request.forms.getunicode('email') or '').strip()
    try:
        cliente_dao.salvar(Cliente(id=None, nome=nome, email=email))
        redirect('/')
    except sqlite3.IntegrityError:
        redirect('/?erro=E-mail+já+cadastrado.')

@get('/editar/<id:int>')
def exibir_edicao_cliente(id: int):
    cliente = cliente_dao.buscar_por_id(id)
    if not cliente:
        redirect('/?erro=Cliente+não+encontrado.')
    return template('cliente_editar', cliente=cliente)

@post('/editar/<id:int>')
def salvar_edicao_cliente(id: int):
    nome = (request.forms.getunicode('nome') or '').strip()
    email = (request.forms.getunicode('email') or '').strip()
    try:
        cliente_dao.salvar(Cliente(id=id, nome=nome, email=email))
        redirect('/')
    except sqlite3.IntegrityError:
        redirect('/?erro=E-mail+pertence+a+outro+cliente.')

@get('/deletar/<id:int>')
def deletar_cliente(id: int):
    try:
        cliente_dao.deletar(id)
    except sqlite3.Error:
        redirect('/?erro=Cliente+possui+pedidos+vinculados.')
    redirect('/')

# --- ROTAS DE PRODUTOS ---
@get('/produtos')
def listar_produtos():
    msg_erro = request.query.get('erro', '')
    return template('produtos', lista_produtos=produto_dao.listar_todos(), msg_erro=msg_erro)

@post('/produtos/cadastrar')
def cadastrar_produto():
    nome = (request.forms.getunicode('nome') or '').strip()
    try:
        preco = float(request.forms.get('preco', 0))
        estoque = int(request.forms.get('estoque', 0))
        produto_dao.salvar(Produto(id=None, nome=nome, preco=preco, estoque=estoque))
        redirect('/produtos')
    except Exception as e:
        redirect(f'/produtos?erro={e}')

@get('/produtos/editar/<id:int>')
def exibir_edicao_produto(id: int):
    produto = produto_dao.buscar_por_id(id)
    if not produto:
        redirect('/produtos?erro=Produto+não+encontrado.')
    return template('produto_editar', produto=produto)

@post('/produtos/editar/<id:int>')
def salvar_edicao_produto(id: int):
    nome = (request.forms.getunicode('nome') or '').strip()
    try:
        preco = float(request.forms.get('preco', 0))
        estoque = int(request.forms.get('estoque', 0))
        produto_dao.salvar(Produto(id=id, nome=nome, preco=preco, estoque=estoque))
        redirect('/produtos')
    except Exception as e:
        redirect(f'/produtos?erro={e}')

@get('/produtos/deletar/<id:int>')
def deletar_produto(id: int):
    try:
        produto_dao.deletar(id)
    except sqlite3.Error:
        redirect('/produtos?erro=Produto+vinculado+a+pedidos.')
    redirect('/produtos')

# --- ROTAS DE PEDIDOS ---
@get('/pedidos')
def listar_pedidos():
    msg_erro = request.query.get('erro', '')
    clientes = cliente_dao.listar_todos()
    produtos = [p for p in produto_dao.listar_todos() if p.estoque > 0]
    pedidos = pedido_dao.listar_com_detalhes()
    return template('pedidos', lista_clientes=clientes, lista_produtos=produtos, lista_pedidos=pedidos, msg_erro=msg_erro)

@post('/pedidos/cadastrar')
def cadastrar_pedido():
    try:
        cliente_id = int(request.forms.get('cliente_id'))
        produto_id = int(request.forms.get('produto_id'))
        quantidade = int(request.forms.get('quantidade', 1))
        
        pedido_dao.criar_pedido_transacional(cliente_id, produto_id, quantidade)
        redirect('/pedidos')
    except Exception as e:
        redirect(f'/pedidos?erro={e}')

if __name__ == '__main__':
    db_mgr.inicializar_tabelas()
    print("Servidor modularizado rodando em http://localhost:8080 ...")
    run(host='localhost', port=8080, debug=True, reloader=True)
```

---

### **Benefícios da Organização Modular**

- **Manutenibilidade**: Alterar a estrutura do modelo `Produto` exige alterar apenas `models/produto.py` e `dao/produto_dao.py`, sem afetar o resto da aplicação.
- **Testabilidade**: É possível escrever testes unitários para a camada de DAO (`ClienteDAO`, `ProdutoDAO`, `PedidoDAO`) importando-os individualmente e passando um banco temporário (`:memory:`).
- **Reutilização de Código**: Qualquer novo script (CLI, API ou tarefa agendada) pode importar `models` e `dao` diretamente sem depender do servidor HTTP.

---

💡 Próxima fase: como implementar **Testes Unitários em Python (usando `unittest` e banco de dados em memória `:memory:`)** para testar as classes `ClienteDAO`, `ProdutoDAO` e `PedidoDAO` sem afetar seu arquivo de banco real.

>[!tip] ⬅️ [[Pratica CRUD Python Sqlite criando relatorios]]
