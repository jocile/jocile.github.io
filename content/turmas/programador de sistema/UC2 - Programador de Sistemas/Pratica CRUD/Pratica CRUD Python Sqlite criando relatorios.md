---
description: "Exemplo prático de um cadastro com Python e banco de dados Sqlite."
tags:
  - pratica
  - python
  - sqlite
  - crud
  - didatica
  - programacao
---

## Gerando um relatório

A geração de um **relatório consolidado de vendas** baseia-se na aplicação da cláusula **`GROUP BY`**, que agrupa registros com valores idênticos em colunas específicas, combinada a funções de agregação como **`SUM()`** (somatório dos valores numéricos) e **`COUNT()`** (contagem de registros).

---

### **1. Como Funciona a Consulta SQL (`DQL`)**

Para consolidar as vendas por cliente, realiza-se um **`LEFT JOIN`** entre a tabela `clientes` e a tabela `pedidos`. O `LEFT JOIN` garante que todos os clientes cadastrados apareçam no relatório, mesmo aqueles que ainda não realizaram nenhuma compra.

A consulta SQL completa fica assim:

```sql
SELECT 
    c.id AS cliente_id,
    c.nome AS cliente_nome,
    c.email AS cliente_email,
    COUNT(p.id) AS total_pedidos,
    COALESCE(SUM(p.quantidade * p.preco_unitario), 0.0) AS total_gasto
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.cliente_id
GROUP BY c.id, c.nome, c.email
ORDER BY total_gasto DESC;
```

#### **Entendendo os Elementos da Consulta:**

* **`SUM(p.quantidade * p.preco_unitario)`**: Multiplica a quantidade pelo preço unitário congelado no momento da venda e soma o total de todos os itens do cliente.
* **`COALESCE(..., 0.0)`**: Substitui o valor `NULL` por `0.0` caso o cliente não tenha nenhum pedido registrado.
* **`GROUP BY c.id, c.nome, c.email`**: Agrupa todas as vendas pelo identificador único e pelos dados do cliente.
* **`ORDER BY total_gasto DESC`**: Classifica o relatório a partir do cliente que mais consumiu (maior faturamento) para o menor.

---

### **2. Filtrando Grupos com a Cláusula `HAVING`**

Se você quiser filtrar o relatório para exibir **apenas clientes com volume de compras acima de um determinado valor** (por exemplo, clientes *VIP* que gastaram mais de R\$ 200,00), deve-se utilizar a cláusula **`HAVING`** após o `GROUP BY` (pois o `WHERE` não pode ser usado com resultados de funções agregadas):

```sql
SELECT 
    c.id AS cliente_id,
    c.nome AS cliente_nome,
    COUNT(p.id) AS total_pedidos,
    SUM(p.quantidade * p.preco_unitario) AS total_gasto
FROM clientes c
INNER JOIN pedidos p ON c.id = p.cliente_id
GROUP BY c.id, c.nome
HAVING SUM(p.quantidade * p.preco_unitario) > 200.0
ORDER BY total_gasto DESC;
```

*(A cláusula `HAVING` aplica o filtro sobre o resultado acumulado do agrupamento).*

---

### **3. Integrando o Relatório no Sistema Web Bottle**

#### **a) Atualização do Template Base (`views/base.tpl`)**

Adicione o novo link no menu de navegação do `base.tpl`:

```html
<nav>
    <a href="/">👤 Clientes</a>
    <a href="/produtos">📦 Produtos</a>
    <a href="/pedidos">🛒 Pedidos</a>
    <a href="/relatorio">📊 Relatório de Vendas</a>
</nav>
```

#### **b) Criando a View do Relatório (`views/relatorio.tpl`)**

Crie o arquivo `views/relatorio.tpl` utilizando o motor `SimpleTemplate` do Bottle:

```html
% rebase('base.tpl', titulo='Relatório Consolidado de Vendas')

<h2>📊 Faturamento Consolidado por Cliente</h2>

% if not relatorio:
    <p>Nenhum dado cadastrado para exibição do relatório.</p>
% else:
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Cliente</th>
                <th>E-mail</th>
                <th>Total de Pedidos</th>
                <th>Valor Total Acumulado</th>
            </tr>
        </thead>
        <tbody>
            % for item in relatorio:
            <tr>
                <td>#{{ item['cliente_id'] }}</td>
                <td><strong>{{ item['cliente_nome'] }}</strong></td>
                <td>{{ item['cliente_email'] }}</td>
                <td>{{ item['total_pedidos'] }} pedido(s)</td>
                <td><strong>R$ {{ "%.2f" % item['total_gasto'] }}</strong></td>
            </tr>
            % end
        </tbody>
    </table>
% end
```

#### **c) Criando a Rota em Python (`app.py`)**

Adicione a rota `/relatorio` no seu arquivo `app.py`:

```python
@get('/relatorio')
def exibir_relatorio_vendas():
    conn = get_connection()
    cursor = conn.cursor()
    
    query = """
        SELECT 
            c.id AS cliente_id,
            c.nome AS cliente_nome,
            c.email AS cliente_email,
            COUNT(p.id) AS total_pedidos,
            COALESCE(SUM(p.quantidade * p.preco_unitario), 0.0) AS total_gasto
        FROM clientes c
        LEFT JOIN pedidos p ON c.id = p.cliente_id
        GROUP BY c.id, c.nome, c.email
        ORDER BY total_gasto DESC;
    """
    
    cursor.execute(query)
    relatorio = cursor.fetchall()
    conn.close()
    
    return template('relatorio', relatorio=relatorio)
```

---

📈 Gostaria de ver como exportar esse relatório consolidado de vendas diretamente para um arquivo **CSV** ou um **DataFrame do Pandas** para análise estatística?

## Exportando para um arquivo csv

Para exportar o relatório consolidado de vendas diretamente para um arquivo CSV, é possível seguir duas abordagens principais:

1. **Via Rota no Bottle (Download direto pelo Navegador)**: O usuário clica em um botão na interface web e o servidor envia a planilha formatada para download automático [cite: 109, 111, 112].
2. **Via Script Python / Pandas (Arquivo local em disco)**: O Python executa a consulta SQL e grava o arquivo `.csv` diretamente no computador [cite: 8, 30, 133].

---

### **Abordagem 1: Download do CSV na Aplicação Web (Bottle)**

Esta abordagem utiliza o módulo nativo `csv` do Python combinado com `io.StringIO` para construir a planilha em memória RAM [cite: 105] e define os cabeçalhos de resposta HTTP (`response.headers`) do Bottle para sinalizar ao navegador que um arquivo deve ser baixado [cite: 109, 111].

#### **1. Adicionar o Botão no Template (`views/relatorio.tpl`)**

Inclua um botão de exportação na página do relatório apontando para a nova rota `/relatorio/exportar-csv`:

```html
% rebase('base.tpl', titulo='Relatório Consolidado de Vendas')

<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
    <h2>📊 Faturamento Consolidado por Cliente</h2>
    <!-- Botão de Download -->
    <a href="/relatorio/exportar-csv" style="background: #198754; color: white; padding: 10px 15px; text-decoration: none; border-radius: 4px; font-weight: bold;">
        📥 Exportar para CSV
    </a>
</div>

<!-- Tabela do relatório -->
<table>
    ...
</table>
```

#### **2. Criar a Rota de Exportação em Python (`app.py`)**

```python
import sqlite3
import csv
import io
from bottle import get, response

DB_NAME = 'meu_banco_de_dados.db'

@get('/relatorio/exportar-csv')
def exportar_relatorio_csv():
    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Consulta SQL para o relatório consolidado de vendas
        query = """
            SELECT 
                c.id AS cliente_id,
                c.nome AS cliente_nome,
                c.email AS cliente_email,
                COUNT(p.id) AS total_pedidos,
                COALESCE(SUM(p.quantidade * p.preco_unitario), 0.0) AS total_gasto
            FROM clientes c
            LEFT JOIN pedidos p ON c.id = p.cliente_id
            GROUP BY c.id, c.nome, c.email
            ORDER BY total_gasto DESC;
        """
        cursor.execute(query)
        relatorio = cursor.fetchall()
        
        # 1. Cria um buffer textual em memória RAM
        output = io.StringIO()
        writer = csv.writer(output, delimiter=';')  # Ponto e vírgula para compatibilidade com o Excel
        
        # 2. Escreve o cabeçalho das colunas
        writer.writerow(['ID Cliente', 'Nome', 'E-mail', 'Total de Pedidos', 'Valor Total Gasto (R$)'])
        
        # 3. Escreve as linhas de dados formatadas
        for linha in relatorio:
            writer.writerow([
                linha,
                linha,
                linha,
                linha,
                f"{linha:.2f}".replace('.', ',')  # Formatação decimal para moeda nacional
            ])
            
        # 4. Configura os cabeçalhos HTTP para acionar o download no navegador
        response.headers['Content-Type'] = 'text/csv; charset=utf-8'
        response.headers['Content-Disposition'] = 'attachment; filename="relatorio_vendas_clientes.csv"'
        
        # Retorna o texto formatado do arquivo CSV
        return output.getvalue()
        
    except sqlite3.Error as e:
        return f"Erro ao gerar o relatório CSV: {e}"
    finally:
        if conn:
            conn.close()
```

---

### **Abordagem 2: Gerar Arquivo CSV Local com Pandas**

Caso o objetivo seja gerar o arquivo `.csv` diretamente no computador para automações ou análises estatísticas internas, pode-se usar a integração nativa entre o `sqlite3` e o **Pandas** :

```python
import sqlite3
import pandas as pd

# 1. Conecta ao banco de dados SQLite
conn = sqlite3.connect('meu_banco_de_dados.db')

# 2. Executa a consulta agregada e carrega o resultado diretamente em um DataFrame
query = """
    SELECT 
        c.id AS 'ID Cliente',
        c.nome AS 'Nome Cliente',
        c.email AS 'E-mail',
        COUNT(p.id) AS 'Total de Pedidos',
        COALESCE(SUM(p.quantidade * p.preco_unitario), 0.0) AS 'Valor Total Gasto (R$ [cite: 8, 30, 56, 133])'
    FROM clientes c
    LEFT JOIN pedidos p ON c.id = p.cliente_id
    GROUP BY c.id, c.nome, c.email
    ORDER BY 'Valor Total Gasto (R$)' DESC;
"""

df_relatorio = pd.read_sql_query(query, conn)
conn.close()

# 3. Exporta o DataFrame diretamente para um arquivo .csv
df_relatorio.to_csv('relatorio_vendas_consolidado.csv', index=False, sep=';', encoding='utf-8-sig')

print("Relatório CSV salvo com sucesso em 'relatorio_vendas_consolidado.csv'!")
```

---

### **Vantagens das Práticas Adotadas**

* **Processamento In-Memory (`io.StringIO`)**: Na rota web do Bottle, a geração do arquivo é feita diretamente na memória sem salvar arquivos temporários desnecessários no disco do servidor [cite: 105, 109].
* **Compatibilidade com Excel**: A utilização do delimitador `;` e do encoding `utf-8-sig` evita que o Microsoft Excel desconfigure a acentuação de caracteres ou misture as colunas ao abrir a planilha [cite: 133, 134].

📈 Quer ver como criar gráficos visuais de barras do faturamento por cliente usando Matplotlib ou Seaborn em Python?

## Criando gráficos visuais

Para criar e exibir **gráficos de barras do faturamento por cliente** na sua aplicação web com **Bottle**, utiliza-se a biblioteca **Matplotlib** combinada ao **Pandas** para extrair os dados agrupados do **SQLite** [cite: 2, 5, 13].

Existem duas abordagens principais para servir imagens de gráficos em aplicações web:

1. **Salvando na Pasta Estática (`static/`)**: O gráfico é gerado e salvo como imagem PNG em disco, sendo servido pela rota de arquivos estáticos do Bottle [cite: 112, 245].
2. **Gerando Dinamicamente em Memória (`io.BytesIO`)**: A imagem é gerada na memória RAM e transmitida diretamente pela rota HTTP em tempo real.

---

### **1. Abordagem 1: Salvando o Gráfico na Pasta Estática (`static/`)**

Esta é a abordagem mais simples e fácil de integrar com a rota estática `/static/<filepath:path>` já configurada [cite: 112, 245].

#### **Passo 1: Configurar o Matplotlib para Servidor (Backend `Agg`)**

Servidores web rodam sem interface gráfica. Por isso, configure o Matplotlib no modo **`Agg`** (não-interativo) antes de importar o `pyplot` para evitar erros de ambiente sem janela:

```python
import matplotlib
matplotlib.use('Agg')  # Desativa a janela interativa do Matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
from pathlib import Path
from bottle import get, template, static_file
```

*(Configuração para geração de gráficos em servidores web).*

#### **Passo 2: Criar a Função de Geração do Gráfico de Barras**

A função executa a consulta agregada com `pd.read_sql_query()`, desenha o gráfico de barras com Matplotlib [cite: 5, 13, 25] e salva a imagem na pasta `static/`:

```python
def gerar_grafico_faturamento():
    conn = sqlite3.connect('meu_banco_de_dados.db')

    # 1. Consulta SQL para faturamento acumulado por cliente
    query = """
        SELECT
            c.nome AS cliente,
            COALESCE(SUM(p.quantidade * p.preco_unitario), 0.0) AS faturamento
        FROM clientes c
        LEFT JOIN pedidos p ON c.id = p.cliente_id
        GROUP BY c.id, c.nome
        ORDER BY faturamento DESC;
    """

    df = pd.read_sql_query(query, conn)
    conn.close()

    # 2. Configura a figura e o tamanho do gráfico
    plt.figure(figsize=(8, 4.5))

    # 3. Desenha o gráfico de barras
    bars = plt.bar(df['cliente'], df['faturamento'], color='#0d6efd', edgecolor='#0a58ca')

    plt.title('Faturamento Total por Cliente (R$)', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Cliente', fontsize=11)
    plt.ylabel('Faturamento (R$)', fontsize=11)
    plt.xticks(rotation=30, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Adiciona os rótulos com os valores exatos no topo de cada barra
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2.0,
            height + (height * 0.01),
            f'R$ {height:.2f}',
            ha='center',
            va='bottom',
            fontsize=9
        )

    plt.tight_layout()

    # 4. Salva a imagem gerada dentro da pasta static/
    caminho_imagem = Path('static') / 'grafico_faturamento.png'
    plt.savefig(caminho_imagem, dpi=150)
    plt.close()  # Fecha a figura para liberar a memória
```

*(Geração e salvamento de gráfico com Pandas e Matplotlib baseados nos materiais) .*

#### **Passo 3: Exibir a Imagem no Template HTML (`views/relatorio.tpl`)**

Basta incluir a tag `<img src="/static/grafico_faturamento.png">` no template de relatório do Bottle :

```html
% rebase('base.tpl', titulo='Relatório e Gráficos de Vendas')

<h2>📊 Painel de Faturamento por Cliente</h2>

<!-- Exibição da Imagem do Gráfico -->
<div style="text-align: center; margin-bottom: 30px;">
    <img src="/static/grafico_faturamento.png" alt="Gráfico de Faturamento por Cliente" style="max-width: 100%; border: 1px solid #dee2e6; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
</div>

<h2>Tabela Consolidada</h2>
<table>
    <thead>
        <tr>
            <th>Cliente</th>
            <th>Faturamento (R$ [cite: 5, 13, 25] [cite: 112])</th>
        </tr>
    </thead>
    <tbody>
        % for item in relatorio:
        <tr>
            <td>{{ item['cliente_nome'] }}</td>
            <td>R$ {{ "%.2f" % item['total_gasto'] }}</td>
        </tr>
        % end
    </tbody>
</table>
```

#### **Passo 4: Atualizar a Rota no Bottle (`app.py`)**

Gere a versão atualizada da imagem sempre que o usuário acessar a página `/relatorio`:

```python
@get('/relatorio')
def exibir_relatorio():
    # 1. Atualiza o gráfico de barras com os dados mais recentes
    gerar_grafico_faturamento()

    # 2. Carrega a tabela consolidada
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.nome AS cliente_nome, COALESCE(SUM(p.quantidade * p.preco_unitario), 0.0) AS total_gasto
        FROM clientes c
        LEFT JOIN pedidos p ON c.id = p.cliente_id
        GROUP BY c.id, c.nome
        ORDER BY total_gasto DESC;
    """)
    relatorio = cursor.fetchall()
    conn.close()

    return template('relatorio', relatorio=relatorio)
```

---

### **2. Abordagem 2: Gerando a Imagem Dinamicamente em Memória (`io.BytesIO`)**

Se você **não quiser criar arquivos em disco**, pode responder a uma rota `/grafico/faturamento.png` diretamente em memória RAM enviando o fluxo de bytes com o cabeçalho `response.content_type = 'image/png'`:

```python
import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
from bottle import get, response

@get('/grafico/faturamento.png')
def grafico_dinamico():
    conn = sqlite3.connect('meu_banco_de_dados.db')
    df = pd.read_sql_query("""
        SELECT c.nome AS cliente, COALESCE(SUM(p.quantidade * p.preco_unitario), 0.0) AS faturamento
        FROM clientes c
        LEFT JOIN pedidos p ON c.id = p.cliente_id
        GROUP BY c.id, c.nome
        ORDER BY faturamento DESC;
    """, conn)
    conn.close()

    # Desenha o gráfico
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(df['cliente'], df['faturamento'], color='#198754')
    ax.set_title('Faturamento por Cliente (R$)', fontweight='bold')
    ax.set_ylabel('R$ Total')
    plt.xticks(rotation=25, ha='right')
    plt.tight_layout()

    # Grava o gráfico no buffer de memória RAM
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', dpi=150)
    plt.close(fig)
    buffer.seek(0)

    # Define o tipo de resposta HTTP como imagem
    response.content_type = 'image/png'
    return buffer.getvalue()
```

E no template HTML, basta incluir a tag apontando diretamente para essa rota:

```html
<img src="/grafico/faturamento.png" alt="Gráfico Dinâmico em Memória">
```

---

💡 Quer ver como integrar uma biblioteca JavaScript no navegador (como **Chart.js**) para criar gráficos interativos com animações e *tooltips* ao passar o mouse sobre as barras?

## Integrando gráficos em JavaScript

Integrar uma biblioteca JavaScript como o **Chart.js** no navegador é a abordagem ideal para criar dashboards modernos, interativos e animados.

Diferente da geração de imagens estáticas no servidor, o **Chart.js** roda diretamente no navegador do cliente: o servidor Bottle fornece apenas os dados no formato **JSON**, e o JavaScript se encarrega de desenhar as barras com animações suaves, renderizar *tooltips* informativos ao passar o mouse e ajustar o tamanho do gráfico automaticamente.

---

### **Como Funciona a Arquitetura**

1. **Backend (Python + Bottle)**: O Bottle cria uma rota de API (`/api/faturamento`) que consulta o banco SQLite, agrupa o faturamento por cliente usando `GROUP BY` e `SUM()`, e retorna um dicionário Python. O Bottle converte automaticamente esse dicionário para JSON.
2. **Frontend (HTML + JavaScript)**: O template HTML carrega a biblioteca **Chart.js** via CDN, faz uma requisição `fetch()` para a API do Bottle e constrói o gráfico interativo dentro de uma tag `<canvas>`.

---

### **Passo 1: Criar a Rota de API de Dados no Python (`app.py`)**

No Bottle, qualquer rota que retorne um dicionário Python é serializada automaticamente no formato **JSON** com o cabeçalho `Content-Type: application/json`:

```python
import sqlite3
from bottle import get, template, run

DB_NAME = 'meu_banco_de_dados.db'

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# 1. ROTA DE API: Retorna os dados agrupados no formato JSON para o Chart.js
@get('/api/faturamento')
def api_faturamento():
    conn = get_connection()
    cursor = conn.cursor()
    
    query = """
        SELECT 
            c.nome AS cliente,
            COALESCE(SUM(p.quantidade * p.preco_unitario), 0.0) AS total_gasto
        FROM clientes c
        LEFT JOIN pedidos p ON c.id = p.cliente_id
        GROUP BY c.id, c.nome
        ORDER BY total_gasto DESC;
    """
    cursor.execute(query)
    resultados = cursor.fetchall()
    conn.close()

    # Separa as colunas em duas listas
    rotulos = [linha['cliente'] for linha in resultados]
    valores = [float(linha['total_gasto']) for linha in resultados]

    # O Bottle converte este dicionário em JSON automaticamente
    return {
        "rotulos": rotulos,
        "valores": valores
    }

# 2. ROTA DA PÁGINA: Renderiza a tela do relatório
@get('/relatorio')
def exibir_relatorio():
    return template('relatorio')

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
```

*(Uso da serialização automática de dicionários em JSON e consultas com agregação baseados nos materiais).*

---

### **Passo 2: Criar o Template com Chart.js (`views/relatorio.tpl`)**

No template `views/relatorio.tpl`, inclua o script do Chart.js via CDN, declare a tag `<canvas>` e utilize o comando nativo `fetch()` do JavaScript para carregar os dados da API:

```html
% rebase('base.tpl', titulo='Dashboard Interativo de Vendas')

<h2>📊 Dashboard Interativo de Faturamento por Cliente</h2>

<!-- Container com a tag Canvas onde o gráfico será desenhado -->
<div style="position: relative; height: 400px; width: 100%; margin-bottom: 30px;">
    <canvas id="graficoFaturamento"></canvas>
</div>

<!-- Importação do Chart.js via CDN -->
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<script>
    // Função para carregar os dados da API e renderizar o gráfico
    async function carregarGrafico() {
        try {
            // 1. Faz a requisição para a rota de API do Bottle
            const resposta = await fetch('/api/faturamento');
            const dados = await resposta.json();

            // 2. Obtém o contexto do elemento Canvas
            const ctx = document.getElementById('graficoFaturamento').getContext('2d');

            # 3. Instancia o gráfico com Chart.js
            new Chart(ctx, {
                type: 'bar', // Tipo do gráfico: barra
                data: {
                    labels: dados.rotulos, // Nomes dos clientes
                    datasets: [{
                        label: 'Faturamento Total (R$)',
                        data: dados.valores, // Valores numéricos
                        backgroundColor: 'rgba(13, 110, 253, 0.75)',
                        borderColor: 'rgba(13, 110, 253, 1)',
                        borderWidth: 1,
                        borderRadius: 5,
                        hoverBackgroundColor: 'rgba(25, 135, 84, 0.85)' // Cor ao passar o mouse
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    animation: {
                        duration: 1200, // Tempo da animação inicial em milissegundos
                        easing: 'easeOutQuart'
                    },
                    plugins: {
                        legend: {
                            display: true,
                            position: 'top'
                        },
                        tooltip: {
                            enabled: true, // Ativa tooltips interativos ao passar o mouse
                            callbacks: {
                                label: function(context) {
                                    let valor = context.raw || 0;
                                    return ' Faturamento: R$ ' + valor.toFixed(2).replace('.', ',');
                                }
                            }
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            ticks: {
                                callback: function(value) {
                                    return 'R$ ' + value;
                                }
                            }
                        }
                    }
                }
            });
        } catch (erro) {
            console.error('Erro ao carregar os dados do gráfico:', erro);
        }
    }

    // Executa a função após o carregamento da página
    document.addEventListener('DOMContentLoaded', carregarGrafico);
</script>
```

---

### **Recursos Obtidos com Essa Integração**

* **Animações de Entrada**: Ao abrir a página, as barras sobem suavemente a partir do zero.
* **Tooltips Personalizados**: Ao passar o ponteiro do mouse sobre qualquer barra, um balão informativo exibe o nome do cliente e o valor formatado em moeda (ex: `R$ 1.250,00`).
* **Hover com Destaque de Cor**: A cor da barra muda dinamicamente para verde quando o usuário passa o mouse.
* **Design Responsivo**: O elemento `<canvas>` ajusta sua largura e altura automaticamente conforme o tamanho da tela ou dispositivo.

---

>[!tip] ⬅️ [[Pratica CRUD Python Sqlite cadastro de pedidos]] | ➡️ [[Chave primaria e chave extrangeira]] | ➡️ [[Pratica CRUD Python Sqlite com POO]]
