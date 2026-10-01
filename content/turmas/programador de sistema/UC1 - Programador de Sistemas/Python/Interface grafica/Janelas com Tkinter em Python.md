---
title: "Janelas com Tkinter em Python"
date: 2026-09-27
draft: false
tags:
  - python
  - tkinter
  - gui
description: "Introdução à biblioteca Tkinter, a ferramenta padrão do Python para criar interfaces gráficas, abordando criação de janelas, widgets e gerenciamento de layouts."
---

Tkinter é a biblioteca padrão do Python para criação de interfaces gráficas. Ele é incluído com a maioria das distribuições do Python, facilitando seu uso sem a necessidade de instalação adicional.

**Vantagens do Tkinter:**
- Simples de aprender e usar.
- Bom para pequenas e médias aplicações.
- Integração direta com o Python.

Tkinter geralmente vem pré-instalado com Python. Para verificar, basta tentar importá-lo:

```python
import tkinter
```

## Criando uma Janela Simples

Vamos começar criando uma janela simples com Tkinter. Primeiro, importamos a biblioteca e criamos uma instância da janela principal.

```python
import tkinter as tk

# Criação da janela principal
root = tk.Tk()
root.title("Minha Primeira Janela")
root.geometry("300x200")

# Iniciando o loop principal
root.mainloop()
```

## Adicionando Widgets

Widgets são os componentes visuais da GUI, como botões, caixas de texto e rótulos. Vamos adicionar alguns widgets à nossa janela.

```python
# Criação de um rótulo
label = tk.Label(root, text="Olá, Tkinter!")
label.pack()

# Criação de um botão
button = tk.Button(root, text="Clique Aqui", command=lambda: print("Botão clicado!"))
button.pack()
```

## Eventos e Manipuladores

Eventos e manipuladores permitem que a interface responda às ações do usuário, como cliques de botão e movimentos do mouse.

**Exemplo de manipulador de eventos:**

```python
def on_button_click():
    print("O botão foi clicado!")

button = tk.Button(root, text="Clique Aqui", command.on_button_click)
button.pack()
```

## Layouts e Organizadores

Tkinter oferece várias opções para organizar os widgets na janela, como `pack`, `grid` e `place`.

**Exemplo usando o `pack`:**

```python
label1 = tk.Label(root, text="Rótulo 1")
label1.pack(side=tk.LEFT)

label2 = tk.Label(root, text="Rótulo 2")
label2.pack(side=tk.RIGHT)
```

**Exemplo usando o `grid`:**

```python
label1 = tk.Label(root, text="Rótulo 1")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Rótulo 2")
label2.grid(row=1, column=1)
```

## Exemplos

![Exemplo de Cadastro de Alunos](Desafio%20cadastrar%20alunos%20com%20janelas.md#Exemplo%20de%20Cadastro%20de%20Alunos)

## Exemplo de listar de notas

Vamos criar uma aplicação simples para adicionar e listar notas.

```python
import tkinter as tk

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicação de Notas")
        self.root.geometry("400x300")

        # Entrada de texto
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)

        # Botão para adicionar nota
        self.add_button = tk.Button(root, text="Adicionar Nota", command=self.add_note)
        self.add_button.pack(pady=5)

        # Área de texto para listar notas
        self.text_area = tk.Text(root, width=50, height=10)
        self.text_area.pack(pady=10)

    def add_note(self):
        note = self.entry.get()
        self.text_area.insert(tk.END, note + "\n")
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()
```

## Referências

Para aprofundar seus conhecimentos em Tkinter, recomendo os seguintes recursos:

- [Documentação oficial do Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Tutoriais e exemplos](https://realpython.com/python-gui-tkinter/)
- [Como Criar uma Interface Gráfica Python c/ CustomTkinter \[RÁPIDO\] - YouTube](https://www.youtube.com/watch?v=Px-DgrQ_wjI)
- [GitHub - nucleonautomation/Gluonix-Designer · GitHub](https://github.com/nucleonautomation/Gluonix-Designer)
- [Tkinter - Tutorial Completo de telas com Python - YouTube](https://www.youtube.com/watch?v=yHdZvQhSRiA)

Desenvolvimento Rápido de Interfaces (RAD):

- [Tkinter - Pygubu Designer - The Basics - YouTube](https://www.youtube.com/watch?v=1FuVPUIayZ8)
