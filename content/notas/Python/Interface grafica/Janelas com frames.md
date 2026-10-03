---
title: Janelas com frames
description: "São uteis para organizar interfaces grandes, dividindo a janela "
tags:
  - python
  - tkinter
  - gui
---
Janelas com frames são uteis para organizar interfaces grandes, dividindo a janela com **`tk.Frame`** (sub-containers). Você pode criar um frame para o topo (menu), um para o meio (conteúdo) e um para o rodapé, aplicando o `pack()` para empilhar esses frames e o `grid()` dentro de cada um deles de forma isolada.

inicialmente defina:

- Que **tipo de tela** você está tentando construir? (Formulário, painel com botões, etc.)
- Você precisa que a tela seja **responsiva** (que os botões estiquem ao maximizar a janela)?

Aqui está um exemplo prático utilizando o conceito de Frames. A melhor técnica para esse caso é criar os dois frames no início e alternar a visibilidade deles usando os comandos `grid()` e `grid_forget()` (que esconde o frame sem apagá-lo da memória).

## Código Prático (Alternando Telas)

Exemplo de uma janela com dois botões, um para exibir um formulário de cadastro, e outro para exibir o que foi cadastrado:

```python
import tkinter as tk
from tkinter import messagebox

# Lista global para armazenar os dados cadastrados
dados_cadastrados = []

def mostrar_tela_cadastro():
    # Esconde a tela de exibição e mostra a de cadastro
    frame_exibicao.grid_forget()
    frame_cadastro.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

def mostrar_tela_exibicao():
    # Esconde a tela de cadastro e mostra a de exibição
    frame_cadastro.grid_forget()
    frame_exibicao.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
    
    # Atualiza o texto da lista com o que foi cadastrado
    # Primeiro limpa o texto antigo
    txt_lista.config(state="normal")
    txt_lista.delete("1.0", tk.END)
    
    # Adiciona os itens atualizados
    if not dados_cadastrados:
        txt_lista.insert(tk.END, "Nenhum registro encontrado.")
    else:
        for i, item in enumerate(dados_cadastrados, 1):
            txt_lista.insert(tk.END, f"{i}. Nome: {item['nome']} | E-mail: {item['email']}\n")
    
    txt_lista.config(state="disabled") # Deixa o texto apenas como leitura

def salvar_cadastro():
    nome = ent_nome.get().strip()
    email = ent_email.get().strip()
    
    if nome == "" or email == "":
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos!")
        return
        
    # Salva na lista
    dados_cadastrados.append({"nome": nome, "email": email})
    messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
    
    # Limpa os campos de entrada
    ent_nome.delete(0, tk.END)
    ent_email.delete(0, tk.END)

# 1. Configuração da Janela Principal
janela = tk.Tk()
janela.title("Sistema de Cadastro Simples")
janela.geometry("400x300")

# 2. Menu de Navegação (Botões Superiores)
btn_nav_cadastro = tk.Button(janela, text="Ir para Cadastro", command=mostrar_tela_cadastro)
btn_nav_cadastro.grid(row=0, column=0, padx=10, pady=10, sticky="we")

btn_nav_exibicao = tk.Button(janela, text="Ver Cadastrados", command=mostrar_tela_exibicao)
btn_nav_exibicao.grid(row=0, column=1, padx=10, pady=10, sticky="we")

# Configura as colunas do topo para dividirem o espaço igualmente
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)


# ==========================================
# 3. FRAME DE CADASTRO (Design da Tela 1)
# ==========================================
frame_cadastro = tk.LabelFrame(janela, text=" Formulário de Cadastro ", padding=10)

lbl_nome = tk.Label(frame_cadastro, text="Nome:")
lbl_nome.grid(row=0, column=0, padx=5, pady=5, sticky="w")
ent_nome = tk.Entry(frame_cadastro, width=30)
ent_nome.grid(row=0, column=1, padx=5, pady=5)

lbl_email = tk.Label(frame_cadastro, text="E-mail:")
lbl_email.grid(row=1, column=0, padx=5, pady=5, sticky="w")
ent_email = tk.Entry(frame_cadastro, width=30)
ent_email.grid(row=1, column=1, padx=5, pady=5)

btn_salvar = tk.Button(frame_cadastro, text="Salvar Dados", command=salvar_cadastro, bg="#4CAF50", fg="white")
btn_salvar.grid(row=2, column=0, columnspan=2, pady=15)


# ==========================================
# 4. FRAME DE EXIBIÇÃO (Design da Tela 2)
# ==========================================
frame_exibicao = tk.LabelFrame(janela, text=" Registros Salvos ", padding=10)

# Componente de texto para listar as informações
txt_lista = tk.Text(frame_exibicao, width=40, height=8, state="disabled")
txt_lista.grid(row=0, column=0, padx=5, pady=5)


# 5. Inicialização
# Define qual tela abre por padrão ao iniciar o programa
mostrar_tela_cadastro()

janela.mainloop()
```

## Como essa estrutura funciona?

- `LabelFrame`: É uma variação do `Frame` comum que já vem com uma borda e um título incorporado (como _"Formulário de Cadastro"_). Ajuda visualmente a separar as seções.
- `grid_forget()`: Esse é o segredo para alternar telas no Tkinter. Quando você clica em "Ver Cadastrados", o script roda `frame_cadastro.grid_forget()`, o que faz a tela de cadastro desaparecer instantaneamente para dar lugar à outra.
- Manipulação do widget `Text`: Na tela de exibição, usamos o `txt_lista.config(state="normal")` para permitir que o Python escreva os nomes cadastrados ali, e logo em seguida mudamos para `"disabled"` para que o usuário final não consiga apagar ou digitar por cima.

## Referências

- [[Janelas com Tkinter em Python]]
- [[Formulario-de-Login-com-Tkinter]]
