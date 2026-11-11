---
tags: [python, flask, supabase, pythonanywhere, banco-de-dados]
aliases: ["Conectar Flask ao Supabase", "API Supabase PythonAnywhere"]
status: "completa"
updated: 2026-11-08
description: "Conectar Aplicativo Flask ao Supabase no PythonAnywhere"
---

Este guia demonstra como integrar um aplicativo **Flask** hospedado no **PythonAnywhere** com o banco de dados do **Supabase** utilizando a biblioteca cliente oficial `supabase-py`.

> [!TIP] Importante: Conexão Restrita
> O PythonAnywhere bloqueia conexões externas diretas na conta gratuita (exceto via HTTP/HTTPS). Por isso, usar a API de Dados (REST) do Supabase é a **única escolha viável** para esta configuração.

---

## 📋 Pré-requisitos

- Conta no [PythonAnywhere](https://www.pythonanywhere.com/)
- Conta no [Supabase](https://supabase.com/)
- Navegador web atualizado

---

## 🔧 Passo 1: Configuração no Supabase

### Acesso ao Painel de Projetos

1. Acesse o painel do [Supabase](https://supabase.com/) e entre no seu projeto [[supabase-docs]]
2. Vá em **Project Settings** (Configurações) > **API** [[supabase-api]]
3. Copie duas informações essenciais:

   | Item | Descrição | Exemplo |
   |------|-----------|---------|
   | **Project URL** | Base da API do Supabase | `https://xxxxxx.supabase.co` |
   | **anon public API Key** | Chave pública de leitura | `eyJhbGci...` |

> [!WARNING] Segurança de Credenciais
> **NUNCA comente credenciais em repositórios públicos!** Use sempre o arquivo `.env` para armazenar variáveis de ambiente.

---

## 🖥️ Passo 2: Configuração no PythonAnywhere

### Instalação de Dependências

No console Bash do seu PythonAnywhere, execute as seguintes comandos:

```bash
# Criar e ativar o ambiente virtual (Python 3.10+ recomendado)
mkvirtualenv meu_env --python=/usr/bin/python3.10
workon meu_env

# Instalar as dependências necessárias
pip install Flask supabase python-dotenv
```

### Configuração de Variáveis de Ambiente

Crie um arquivo `.env` no diretório do seu app (ex: `/home/seu_usuario/mysite`):

```bash
sudo nano /home/seu_usuario/mysite/.env
```

Adicione o conteúdo:

```ini
SUPABASE_URL=https://xxxxxx.supabase.co
SUPABASE_KEY=eyJhbGci...
```

> [!CAUTION] Código com Cuidado
> Este arquivo contém suas credenciais. Mantenha-o no servidor e nunca exponha-as publicamente.

---

## 🐍 Passo 3: Código do Aplicativo Flask

### Estrutura Principal (`flask_app.py`)

Inicialize o cliente do Supabase utilizando variáveis de ambiente carregadas:

```python
import os
from flask import Flask, jsonify
from dotenv import load_dotenv
from supabase import create_client, Client

# Carrega as variáveis do arquivo .env
load_dotenv()

app = Flask(__name__)

# Inicializa o cliente do Supabase
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

@app.route('/')
def index():
    """Endpoint de saúde e verificação de conexão"""
    return jsonify({
        "status": "App conectado ao Supabase com sucesso!",
        "method": os.environ.get("SUPABASE_URL")
    })

@app.route('/dados', methods=['GET'])
def buscar_dados():
    """Endpoint para consultar dados da tabela 'usuarios'"""
    try:
        # Exemplo de consulta: buscando todos os registros
        response = supabase.table('usuarios').select('*').execute()
        return jsonify({
            "data": response.data,
            "success": True
        })
    except Exception as e:
        return jsonify({
            "erro": str(e),
            "traceback": repr(e.__traceback__)
        }), 500

# IMPORTANTE: No PythonAnywhere, app.run() só deve ser executado no escopo global
if __name__ == '__main__':
    app.run(debug=True)
```

---

## 🌐 Passo 4: Configuração da Aba "Web" no PythonAnywhere

### WSGI Configuration File

Para colocar o app no ar, edite manualmente o arquivo de configuração WSGI:

1. No painel **Web** do PythonAnywhere, clique em **"WSGI configuration file"**
2. Substitua pelo conteúdo abaixo:

```python
import sys
import os

# Caminho absoluto do seu aplicativo
path = '/home/seu_usuario/mysite'
if path not in sys.path:
    sys.path.append(path)

# Carrega variáveis de ambiente antes de importar o app
from dotenv import load_dotenv
load_dotenv(os.path.join(path, '.env'))

from flask_app import app as application  # noqa
```

> [!TIP] Caminho Correto
> Verifique no PythonAnywhere qual é o caminho completo exato do seu projeto. O padrão é `/home/seu_usuario/mysite`.

---

## 🚀 Passo 5: Finalização e Testes

### Iniciar Aplicativo em Produção

1. Clique em **Reload** no topo da página Web
2. Faça uma solicitação de teste ao seu app:

   | Endpoint | Método | Esperado |
   |----------|--------|----------|
   | `/` | GET | Status de conexão OK |
   | `/dados` | GET | Dados retornados do Supabase |

### Troubleshooting Comum

| Problema | Causa Provável | Solução |
|----------|----------------|---------|
| Timeout ao carregar | Rede lenta ou carga excessiva | Reduza o número de registros consultados |
| Erro 502/504 | WSGI mal configurado ou app não importado | Revise a sintaxe do WSGI file |
| Conexão rejeitada | Credenciais inválidas | Verifique URL e Key no `.env` |

---

## ❓ Questões Frequentes

### Q: Posso usar SQLAlchemy/URI ao invés da API REST?

> [!INFO] Alternativa PostgreSQL Direto
> Você **pode**, mas enfrenta limitações: o PythonAnywhere bloqueia conexões SQL externas na conta gratuita. O método `supabase-py` via REST é **exclusivamente recomendado**.

### Q: Por que preciso de python-dotenv?

O `python-dotenv` é necessário para carregar o arquivo `.env` antes de inicializar o Flask app, garantindo que as credenciais do Supabase sejam acessadas no ambiente de produção.

---

## 🔗 Recursos Externos

- [Documentação oficial do Supabase](https://supabase.com/docs/)
- [Guia de integração Flask/Supabase](https://supabase.com/docs/guides/getting-started/quickstarts/flask)
- [Ajuda PythonAnywhere - Flask](https://help.pythonanywhere.com/pages/Flask/)

---

> [!NOTE] Observações Finais
> Este tutorial cobre a configuração básica. Para integrações mais complexas (CRUD completo, autenticação, etc.), consulte os recursos externos acima ou adicione endpoints adicionais conforme necessário.
