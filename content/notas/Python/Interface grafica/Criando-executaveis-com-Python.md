---
title: "Criando arquivos executáveis (.exe) com Python"
date: 2026-09-27
draft: false
tags:
  - python
  - tkinter
  - pyinstaller
description: "Aprenda a criar arquivos executáveis (.exe) a partir de aplicações Python utilizando a biblioteca PyInstaller para facilitar o compartilhamento."
---

Para criar um arquivo executável (.exe) a partir de uma aplicação Python, você pode usar a biblioteca **PyInstaller**. Essa é a biblioteca mais comum para essa finalidade, permitindo que você compartilhe suas aplicações com outras pessoas que não possuem Python instalado em suas máquinas.

### **Passo a passo para criar um executável:**

1. **Instalar o PyInstaller:** Abra o prompt de comando (CMD) e execute o comando `pip install pyinstaller`. Se você já tiver o PyInstaller instalado, uma mensagem informando isso será exibida.
    
2. **Navegar até o diretório do projeto:** Utilize o comando `cd` para acessar a pasta onde o arquivo Python da sua aplicação está localizado.
    
3. **Converter o arquivo .py em executável:** Execute o comando `pyinstaller nome_do_arquivo.py`. Isso criará várias pastas e arquivos dentro do diretório do seu projeto, incluindo uma pasta chamada "dist".

>[!success] Comando: `python -m PyInstaller .\arquivo.py --onefile -w`

4. **Localizar o arquivo .exe:** Dentro da pasta "dist", você encontrará uma pasta com o nome do seu arquivo .py. Dentro dessa pasta estará o arquivo executável com a extensão .exe.

### **Opções adicionais:**

- **Criar um único arquivo executável:** Utilize a flag `--onefile` ao executar o PyInstaller. Isso consolidará todos os arquivos necessários em um único arquivo .exe, facilitando o compartilhamento. Exemplo: `pyinstaller --onefile nome_do_arquivo.py`.
    
- **Suprimir o console:** Utilize a flag `--windowed` (ou `-w`) para impedir que o console seja aberto junto com a aplicação. Isso é útil para aplicações que possuem interface gráfica e não precisam exibir o console. Exemplo: `pyinstaller --onefile --windowed nome_do_arquivo.py`.

### **Bibliotecas para interfaces gráficas:**

- **Tkinter:** Biblioteca padrão do Python para criar interfaces gráficas. É simples de usar e já vem instalada com o Python. Para criar uma janela básica com Tkinter, importe a biblioteca, crie um objeto de janela e inicie o loop de eventos com `window.mainloop()`.
    
- **CustomTkinter:** Biblioteca que oferece uma aparência mais moderna para as interfaces criadas com Tkinter. Para utilizá-la, instale com `pip install customtkinter` e importe a biblioteca em seu código.

### **Outras observações:**

- As fontes fornecidas não mencionam especificamente o termo "Criar arquivos executáveis (.exe)". No entanto, as informações sobre a criação de arquivos .exe a partir de aplicações Python usando o PyInstaller foram extraídas do vídeo sobre a conversão de aplicações Tkinter em arquivos executáveis.
    
- As fontes também fornecem informações sobre a criação de interfaces gráficas com Tkinter e CustomTkinter, o que pode ser útil para desenvolver aplicações que serão convertidas em executáveis.
    
- É importante lembrar que, para compartilhar o executável com outras pessoas, elas precisarão ter as bibliotecas utilizadas no projeto instaladas em seus computadores, a menos que você utilize a flag `--onefile` do PyInstaller.

### Referências

[PyInstaller Manual](https://pyinstaller.org/en/stable/)

![Convert Tkinter Python App to Executable (.Exe) File \[pyinstaller\] - YouTube](https://www.youtube.com/watch?v=Iv_dECet_oM&list=PLs3IFJPw3G9KL3huzPS7g-0PCbS7Auc7I&index=15)
