---
title: Cadastro De Alunos Com Poo
description: Vamos organizar o código em classes para torná-lo mais modular e fácil
  de manter. Criaremos uma classe StudentApp que gerenciará toda a interface e a lógica…
date: '2026-09-26'
draft: false
tags:
- programador
publish: false
---

Vamos organizar o código em classes para torná-lo mais modular e fácil de manter. Criaremos uma classe `StudentApp` que gerenciará toda a interface e a lógica do aplicativo.

### Cadastro de Alunos com Tkinter e organizado em classes

```python
import tkinter as tk
from tkinter import messagebox
import os

class StudentApp:
 def __init__(self, janela):
 self.janela = janela
 self.janela.title("Cadastro de Alunos")
 self.janela.geometry("400x400")

 # Lista para armazenar os dados dos alunos
 self.students = []

 # Criando a interface
 self.create_widgets()

 def create_widgets(self):
 # Campos para entrada de dados
 tk.Label(self.janela, text="Nome:").pack()
 self.name_entry = tk.Entry(self.janela)
 self.name_entry.pack()

 tk.Label(self.janela, text="Endereço:").pack()
 self.address_entry = tk.Entry(self.janela)
 self.address_entry.pack()

 tk.Label(self.janela, text="Turma:").pack()
 self.class_entry = tk.Entry(self.janela)
 self.class_entry.pack()

 # Botões para interações
 tk.Button(self.janela, text="Cadastrar", command=self.add_student).pack(pady=10)
 tk.Button(self.janela, text="Exibir Lista", command=self.show_students).pack(pady=10)
 tk.Button(self.janela, text="Salvar Lista", command=self.save_students).pack(pady=10)
 tk.Button(self.janela, text="Carregar Lista", command=self.load_students).pack(pady=10)

 # Área de texto para exibir a lista de alunos
 self.text_area = tk.Text(self.janela, width=50, height=10)
 self.text_area.pack(pady=10)

 def add_student(self):
 name = self.name_entry.get()
 address = self.address_entry.get()
 student_class = self.class_entry.get()

 if name and address and student_class:
 student_data = f"Nome: {name}, Endereço: {address}, Turma: {student_class}"
 self.students.append(student_data)

 # Limpar os campos de entrada
 self.name_entry.delete(0, tk.END)
 self.address_entry.delete(0, tk.END)
 self.class_entry.delete(0, tk.END)

 # Atualizar a área de texto
 self.show_students()
 else:
 messagebox.showwarning("Entrada Inválida", "Por favor, preencha todos os campos!")

 def show_students(self):
 self.text_area.delete(1.0, tk.END)
 for student in self.students:
 self.text_area.insert(tk.END, student + "\n")

 def save_students(self):
 if self.students:
 with open("students.txt", "w") as file:
 for student in self.students:
 file.write(student + "\n")
 messagebox.showinfo("Sucesso", "Dados dos alunos salvos com sucesso!")
 else:
 messagebox.showwarning("Sem Dados", "Nenhum dado de aluno para salvar!")

 def load_students(self):
 if os.path.exists("students.txt"):
 with open("students.txt", "r") as file:
 loaded_students = file.readlines()
 self.students = [student.strip() for student in loaded_students]
 self.show_students()
 else:
 messagebox.showwarning("Arquivo Não Encontrado", "Nenhum arquivo de dados encontrado!")

if __name__ == "__main__":
 janela = tk.Tk()
 app = StudentApp(janela)
 janela.mainloop()
```

### Explicação do Código Organizado em Classes

1. **Classe `StudentApp`**:
 - O método `__init__` inicializa a janela principal e a lista de alunos.
 - `create_widgets` cria e organiza todos os widgets na janela.
 - `add_student` adiciona um aluno à lista de alunos.
 - `show_students` exibe a lista de alunos na área de texto.
 - `save_students` salva a lista de alunos em um arquivo de texto.
 - `load_students` carrega a lista de alunos de um arquivo de texto.

2. **Método `create_widgets`**:
 - Cria rótulos e campos de entrada para nome, endereço e turma.
 - Cria botões para cadastrar, exibir, salvar e carregar a lista de alunos.
 - Cria uma área de texto para exibir a lista de alunos.

3. **Funções de Manipulação de Dados**:
 - `add_student`: Adiciona um aluno à lista e atualiza a área de texto.
 - `show_students`: Limpa e insere os dados dos alunos na área de texto.
 - `save_students`: Salva os dados dos alunos em um arquivo de texto.
 - `load_students`: Carrega os dados dos alunos de um arquivo de texto.

4. **Execução do Aplicativo**:
 - Criamos uma instância da classe `StudentApp` e iniciamos o loop principal do Tkinter com `janela.mainloop()`.

#programador/desafios /Python 