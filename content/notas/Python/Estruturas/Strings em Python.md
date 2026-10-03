---
title: Strings em Python
description: "Vamos abordar desde conceitos básicos até funcionalidades avançadas, segredos e boas práticas"
tags:
  - python
  - programacao
  - strings
---

As strings são uma parte essencial da programação em Python, especialmente para iniciantes. Entender como criar, manipular e formatar strings é fundamental para escrever códigos eficientes e legíveis.

Neste artigo, vamos explorar tudo o que você precisa saber sobre string em Python, da criação até a formatação. Vamos abordar desde conceitos básicos até funcionalidades avançadas, segredos e boas práticas para evitar erros comuns.

## O que é uma string?

Uma string em Python, também conhecida como *str*, é uma sequência de caracteres que representa texto. Strings são fundamentais na programação, pois permitem a manipulação de dados textuais de forma eficiente e flexível. Vamos explorar como criar e utilizar strings em Python.

### Criando uma string em Python

Para criar uma string em Python, você pode usar aspas simples (`'`) ou aspas duplas (`"`). Ambas as formas são válidas e reconhecidas pela linguagem. A única regra é que você deve abrir e fechar a string com o mesmo tipo de aspas.

```python
# Uma palavra
minha_string = 'Olá'
print(minha_string)  # Saída: Olá

# Uma frase inteira
minha_frase = "Olá, Mundo!"
print(minha_frase)  # Saída: Olá, Mundo!

# Também é possível usar aspas duplas
outra_frase = "Python é ótimo"
print(outra_frase)  # Saída: Python é ótimo
```

### Por que usar aspas simples ou duplas?

A escolha entre aspas simples e duplas pode depender do contexto. Por exemplo, se você precisar incluir aspas dentro da string, pode usar o tipo oposto para evitar conflitos:

```python
# Usando aspas simples dentro de uma string com aspas duplas
frase_com_aspas = "Ele disse: 'Olá, Mundo!'"
print(frase_com_aspas)  # Saída: Ele disse: 'Olá, Mundo!'

# Usando aspas duplas dentro de uma string com aspas simples
frase_com_aspas_duplas = 'Ela respondeu: "Tudo bem?"'
print(frase_com_aspas_duplas)  # Saída: Ela respondeu: "Tudo bem?"
```

### Imprimindo uma string

Para exibir uma string na saída, você pode simplesmente usar a função `print()`. No Jupyter Notebook, apenas colocar a string em uma célula também a exibirá, mas a maneira correta e mais universal é usar `print()`:

```python
# Imprimindo strings
print('Olá Mundo 1')  # Saída: Olá Mundo 1
print('Olá Mundo 2')  # Saída: Olá Mundo 2
print('Use \n para quebrar a linha')  # Saída: Use 
                                      #        para quebrar a linha
print('\n')  # Saída: (quebra de linha)
print('Entendeu?')  # Saída: Entendeu?
```

## Manipulação de strings em Python

Manipular strings em Python é uma habilidade essencial para qualquer programador, especialmente para iniciantes. Strings são sequências de texto que podem ser manipuladas de diversas maneiras. Vamos explorar três operadores fundamentais para trabalhar com strings em Python: o operador `+`, o operador `*` e o operador `in`. Entender como cada um deles funciona permitirá que você manipule strings de forma eficiente e eficaz.

### O operador +

O operador `+` em Python é utilizado para concatenar strings, ou seja, ele junta duas ou mais strings em uma única sequência de caracteres. Por exemplo:

```python
# Definindo duas strings
string1 = "Olá"
string2 = "Mundo"

# Concatenando as strings
resultado = string1 + " " + string2

# Exibindo o resultado
print(resultado)  # Saída: Olá Mundo
```

Neste exemplo, *string1* captura “Olá” e *string2* captura “Mundo”. Ao usar o operador `+`, adicionamos um espaço entre as duas palavras para que não fiquem juntas. Assim, o resultado é “Olá Mundo”.

### Por que usar o operador +?

A concatenação de strings é útil quando você precisa combinar várias partes de texto em uma única mensagem, como ao gerar saudações personalizadas ou criar mensagens dinâmicas baseadas em variáveis.

### Possíveis erros e como evitá-los

Um erro comum ao usar o operador `+` é tentar concatenar uma string com um número diretamente, o que resulta em um `TypeError`. Para evitar isso, converta o número para string usando a função `str()`:

```python
# Exemplo de erro
numero = 5
# print("O número é: " + numero)  # Isso causará um TypeError

# Correção
print("O número é: " + str(numero))  # Saída: O número é: 5
```

### O operador *

O operador `*` em Python é utilizado para repetir uma string um número específico de vezes. Vamos ver um exemplo prático:

```python
# Definindo uma string
string = "Python"

# Repetindo a string 3 vezes
resultado = string * 3

# Exibindo o resultado
print(resultado)  # Saída: PythonPythonPython
```

### Por que usar o operador *?

Repetir strings pode ser útil em situações como criar linhas de separação em um texto ou gerar padrões repetitivos. É uma maneira rápida de manipular strings sem precisar de loops adicionais.

### Possíveis erros e como evitá-los

Um erro comum ao usar o operador `*` é tentar multiplicar uma string por um valor não inteiro, o que resulta em um `TypeError`. Certifique-se de que o valor de multiplicação seja sempre um número inteiro.

```python
# Exemplo de erro
# print("Python" * 2.5)  # Isso causará um TypeError

# Correção
print("Python" * 2)  # Saída: PythonPython
```

### O operador in

O operador `in` em Python é utilizado para verificar se uma substring está presente dentro de uma string maior. Ele retorna `True` se a substring for encontrada e `False` caso contrário.

```python
# Definindo uma string
frase = "Estou aprendendo Python na Asimov Academy"

# Verificando se a substring está presente
resultado = "Python" in frase

# Exibindo o resultado
print(resultado)  # Saída: True
```

### Por que usar o operador in?

O operador `in` é útil para buscas e verificações dentro de strings, como verificar se uma palavra específica está presente em um texto.

### Possíveis erros e como evitá-los

Um erro comum ao usar o operador `in` é esquecer que ele é sensível a maiúsculas e minúsculas. Mas, para evitar problemas, você pode converter ambas as strings para minúsculas antes de fazer a verificação.

```python
# Exemplo de erro
frase = "Estou aprendendo Python na Asimov Academy"
# print("python" in frase)  # Isso retornará False

# Correção
print("python" in frase.lower())  # Saída: True
```

## Funções do Python para strings

As strings são fundamentais na programação em Python, representando texto e informações textuais, e essa linguagem oferece várias funções para manipular strings de forma eficiente. Vamos explorar duas funções essenciais: `str()` e `len()`.

### Criando uma string com str()

A função `str()` é usada para converter um valor em uma string, útil para garantir que um valor seja tratado como texto, independentemente de seu tipo original. Veja um exemplo:

```python
# Exemplo de uso da função str()
numero = 50
texto = "O número é: " + str(numero)
print(texto)  # Saída: O número é: 50
```

#### Por que usar a função str()?

A função `str()` é essencial para a conversão de diferentes tipos de dados em strings, especialmente ao trabalhar com entradas de usuário ou dados de arquivos.

### Verificando o tamanho de uma string com len()

A função `len()` retorna o tamanho de uma string, ou seja, o número de caracteres que ela contém. Veja um exemplo:

```python
# Exemplo de uso da função len()
texto = "Python é incrível!"
tamanho = len(texto)
print(f"O texto tem {tamanho} caracteres.")  # Saída: O texto tem 17 caracteres.
```

### Por que usar a função len()?

A função `len()` é útil para várias operações que dependem do tamanho de uma string, como validação de senha ou formatação de texto.

### Possíveis erros ao usar a função len()

Tentar aplicar `len()` a tipos de dados que não são sequências resultará em `TypeError`. Portanto, verifique sempre se o valor passado para `len()` é uma string ou outra sequência.

```python
# Exemplo de erro ao usar len() em um número
# numero = 123
# tamanho = len(numero)  # Isso causará um TypeError

# Correção
texto = str(123)
tamanho = len(texto)
print(f"O número tem {tamanho} caracteres.")  # Saída: O número tem 3 caracteres.
```

## Indexação de strings em Python

Indexar strings em Python é uma habilidade fundamental, permitindo acessar e manipular partes específicas de uma string. Vamos explorar como retornar um caractere específico, realizar *slicing* e até mesmo inverter uma string.

### Retornando um caractere da string

Para retornar um caractere específico de uma string, utilizamos colchetes `[]` e o índice do caractere desejado. Lembre-se de que a indexação começa em 0. Vamos ver um exemplo:

```python
# Definindo uma string
s = 'Olá Mundo'

# Retornando o primeiro caractere
print(s[0])  # Saída: 'O'

# Retornando o segundo caractere
print(s[1])  # Saída: 'l'

# Retornando o terceiro caractere
print(s[2])  # Saída: 'á'
```

### Utilizando índices negativos

Podemos usar índices negativos para acessar caracteres a partir do final da string:

```python
# Definindo uma string
s = 'Olá Mundo'

# Retornando o último caractere
print(s[-1])  # Saída: 'o'

# Retornando o penúltimo caractere
print(s[-2])  # Saída: 'd'
```

### Slicing de strings

Slicing permite acessar uma subsequência de caracteres usando a notação `s[início:fim]`. Vamos ver exemplos:

```python
# Definindo uma string
s = 'Olá Mundo'

# Retornando todos os caracteres a partir do índice 1
print(s[1:])  # Saída: 'lá Mundo'

# Retornando os caracteres do índice 1 ao 4 (excluindo o 4)
print(s[1:4])  # Saída: 'lá '

# Retornando os primeiros 5 caracteres
print(s[:5])  # Saída: 'Olá M'
```

### Slicing com índices negativos

Slicing com índices negativos permite acessar elementos a partir do final da string:

```python
# Definindo uma string
s = 'Olá Mundo'

# Retornando os últimos 5 caracteres
print(s[-5:])  # Saída: ' Mundo'

# Retornando os caracteres do índice -5 ao -1 (excluindo o -1)
print(s[-5:-1])  # Saída: ' Mund'
```

### Invertendo uma string em Python

Inverter uma string pode ser feito facilmente com slicing e passo negativo:

```python
# Definindo uma string
s = 'Olá Mundo'

# Invertendo a string
print(s[::-1])  # Saída: 'odnuM álO'
```

Inverter uma string é útil em diversas situações, como verificar palíndromos. Vamos ver um exemplo:

```python
# Verificando se uma palavra é um palíndromo
palavra = 'arara'
if palavra == palavra[::-1]:
    print(f'{palavra} é um palíndromo')  # Saída: arara é um palíndromo
else:
    print(f'{palavra} não é um palíndromo')
```

## Métodos de strings em Python

Python oferece uma vasta gama de métodos para trabalhar com strings de forma eficiente. Vamos explorar alguns dos mais úteis para manipular strings.

### Primeira letra maiúscula com .capitalize()

O método `.capitalize()` transforma a primeira letra de uma string em maiúscula e todas as outras em minúsculas. Por exemplo:

```python
texto = "python é INCRÍVEL!"
texto_capitalizado = texto.capitalize()
print(texto_capitalizado)  # Saída: "Python é incrível!"
```

### Primeira letra maiúscula com .title()

O método `.title()` coloca a primeira letra de cada palavra em maiúscula. Isto é ideal para formatar títulos e nomes próprios:

```python
titulo = "aprendendo python na asimov academy"
titulo_formatado = titulo.title()
print(titulo_formatado)  # Saída: "Aprendendo Python Na Asimov Academy"
```

### Invertendo a capitalização com .swapcase()

O método `.swapcase()` inverte a capitalização de cada letra na string:

```python
texto = "Python É Incrível!"
texto_invertido = texto.swapcase()
print(texto_invertido)  # Saída: "pYTHON é INCRÍVEL!"
```

### Texto em maiúsculo com .upper()

O método `.upper()` converte todos os caracteres de uma string para maiúsculas:

```python
texto = "python é incrível!"
texto_maiusculo = texto.upper()
print(texto_maiusculo)  # Saída: "PYTHON É INCRÍVEL!"
```

### Texto em minúsculo com .lower()

O método `.lower()` converte todos os caracteres de uma string para minúsculas:

```python
texto = "Python É Incrível!"
texto_minusculo = texto.lower()
print(texto_minusculo)  # Saída: "python é incrível!"
```

### Contando substrings com .count()

O método `.count()` conta o número de ocorrências de uma substring dentro de uma string:

```python
texto = "Hoje em dia todo dia é um novo dia. Mais um dia chega. Dia!"
contagem = texto.count('dia')
print(contagem)  # Saída: 4
```

### Verificando final de uma string com .endswith()

O método `.endswith()` verifica se uma string termina com uma determinada substring:

```python
arquivo = "relatorio_final.pdf"
verificacao = arquivo.endswith('.pdf')
print(verificacao)  # Saída: True
```

### Verificando início de uma string com .startswith()

O método `.startswith()` verifica se uma string começa com uma determinada substring:

```python
arquivo = "2023_relatorio_final.pdf"
verificacao = arquivo.startswith('2023')
print(verificacao)  # Saída: True
```

### Buscando uma substring com .find()

O método `.find()` retorna o índice da primeira ocorrência de uma substring dentro de uma string. Se não for encontrada, retorna -1:

```python
texto = "Python é incrível!"
indice = texto.find('incrível')
print(indice)  # Saída: 10
```

### Substituindo caracteres com .replace()

O método `.replace()` substitui todas as ocorrências de uma substring por outra:

```python
texto = "Estou estudando Javascript!"
texto_corrigido = texto.replace('Javascript', 'Python')
print(texto_corrigido)  # Saída: "Estou estudando Python!"
```

### Removendo espaços em branco com .strip()

O método `.strip()` remove espaços em branco do início e do fim de uma string:

```python
texto = "   Python é incrível!   "
texto_limpo = texto.strip()
print(texto_limpo)  # Saída: "Python é incrível!"
```

### Encontrando index com .index()

O método `.index()` retorna o índice da primeira ocorrência de uma substring dentro de uma string, mas gera erro se não for encontrada:

```python
texto = "Python é incrível!"
indice = texto.index('incrível')
print(indice)  # Saída: 10
```

## Identificação de caracteres de strings

Identificar e classificar caracteres em strings é essencial para garantir a integridade dos dados. Python oferece vários métodos para essa tarefa, como `str.isalnum()`, `str.isalpha()`, `str.isdigit()`, `str.islower()` e `str.istitle()`. Vamos entender cada um desses métodos.

### str.isalnum()

Verifica se todos os caracteres de uma string são alfanuméricos (letras ou números):

```python
texto = "Python3"
print(texto.isalnum())  # Saída: True

texto2 = "Python 3"
print(texto2.isalnum())  # Saída: False
```

### str.isalpha()

Verifica se todos os caracteres de uma string são letras:

```python
texto = "Python"
print(texto.isalpha())  # Saída: True

texto2 = "Python3"
print(texto2.isalpha())  # Saída: False
```

### str.isdigit()

Verifica se todos os caracteres de uma string são dígitos:

```python
texto = "12345"
print(texto.isdigit())  # Saída: True

texto2 = "12345a"
print(texto2.isdigit())  # Saída: False
```

### str.islower()

Verifica se todos os caracteres alfabéticos de uma string estão em minúsculas:

```python
texto = "python"
print(texto.islower()) # Saída: True

texto2 = "Python"
print(texto2.islower()) # Saída: False
```

### str.istitle()

Verifica se a string está no formato de título, ou seja, se cada palavra começa com uma letra maiúscula seguida de letras minúsculas.

```python
texto = "Programação Python"
print(texto.istitle()) # Saída: True

texto2 = "Programação python"
print(texto2.istitle()) # Saída: False
```

## Formatação de strings

A capacidade de inserir variáveis e formatar texto de maneira clara e eficiente pode fazer uma grande diferença na legibilidade e funcionalidade do seu código. A seguir, temos duas maneiras populares de formatar uma string em Python: usando o método `.format()` e f-strings.

## Formatação com .format

O método `.format()` permite que você insira variáveis em uma string de maneira organizada e legível, substituindo chaves `{}` em uma string pelo valor das variáveis passadas como argumentos. Segue um exemplo simples:

```python
nome = "Adriano"
idade = 31
mensagem = "Meu nome é {} e eu tenho {} anos.".format(nome, idade)
print(mensagem)
```

Aqui, a string *“Meu nome é {} e eu tenho {} anos.”* contém dois pares de chaves `{}`. O método `.format()` substitui o primeiro par pelo valor da variável `nome` e o segundo par pelo valor da variável `idade`. O resultado é a string *“Meu nome é Adriano e eu tenho 31 anos.”*.

### Por que usar o método .format?

Usar o método `.format()` tem várias vantagens:

1. **Legibilidade**: o código fica mais legível e organizado.
2. **Flexibilidade**: você pode formatar números, datas e outros tipos de dados de maneira específica.
3. **Reutilização**: a mesma string pode ser reutilizada com diferentes valores de variáveis.

### Possíveis erros e como evitá-los

Ao usar o método `.format()`, é importante garantir que o número de chaves `{}` na string corresponda ao número de argumentos passados para o método. Caso contrário, você receberá um erro `IndexError`. Além disso, certifique-se de que os tipos de dados sejam compatíveis com a formatação especificada.

## Formatação com f-string

As *f-strings*, introduzidas no Python 3.6, são uma maneira mais moderna e conveniente de formatar strings, pois permitem a inserção direta de variáveis dentro de uma string, tornando o código mais conciso e legível.

### Como funcionam as f-strings?

Para usar uma f-string, basta prefixar a string com a letra `f` e colocar as variáveis entre chaves `{}`. Observe este exemplo simples:

```python
nome = "Adriano"
idade = 31
mensagem = f"Meu nome é {nome} e eu tenho {idade} anos."
print(mensagem)
```

Neste código, a string *f”Meu nome é {nome} e eu tenho {idade} anos.”* insere diretamente os valores das variáveis `nome` e `idade` na string. Dessa forma, o resultado é a string “Meu nome é Adriano e eu tenho 31 anos.”.

### Por que usar f-strings?

As f-strings têm várias vantagens:

1. **Simplicidade**: o código é mais curto e fácil de escrever.
2. **Legibilidade**: a inserção direta de variáveis torna o código mais fácil de entender.
3. **Eficiência**: as f-strings são mais rápidas do que o método `.format()`.

### Possíveis erros e como evitá-los

Ao usar f-strings, é importante garantir que as variáveis dentro das chaves `{}` existam e sejam válidas, pois, do contrário, você receberá um erro `NameError`. Além disso, certifique-se de que os tipos de dados sejam compatíveis com a formatação especificada.

## Conversões entre lista e string em Python

No mundo da programação, especialmente em Python, é comum a necessidade de converter dados entre diferentes tipos. Um exemplo clássico é a conversão entre listas e strings, que vamos explorar a seguir como realizá-la utilizando métodos como `.join()`, `.partition()` e `.split()`.

### Convertendo uma lista em string com .join()

O método `.join()` é extremamente útil quando precisamos transformar uma lista de elementos em uma única string, separando cada elemento por um delimitador específico.

### Exemplo de uso do .join()

Vamos considerar uma lista de palavras que queremos unir em uma única string, separadas por espaços:

```python
# Lista de palavras
palavras = ["Olá", "mundo", "Python", "é", "incrível"]

# Convertendo a lista em string
frase = " ".join(palavras)

# Exibindo a string resultante
print(frase)
```

### Por que usar .join()?

O método `.join()` é eficiente e flexível. Ele permite que você escolha o delimitador que deseja usar para separar os elementos da lista. Por exemplo, você pode usar uma vírgula, um ponto e vírgula ou qualquer outro caractere:

```python
# Usando vírgula como delimitador
palavras = ["Olá", "mundo", "Python", "é", "incrível"]

frase_com_virgula = ", ".join(palavras)

print(frase_com_virgula)
```

## Convertendo uma string em lista com .partition()

O método `.partition()` converte uma string em uma lista dividindo-na em três partes: a parte antes do separador, o próprio separador e a parte após o separador.

### Exemplo de uso do .partition()

Vamos considerar uma string que queremos dividir em uma lista de três partes:

```python
# String de exemplo
frase = "Python é incrível"

# Convertendo a string em lista usando .partition()
partes = frase.partition("é")

# Exibindo a lista resultante
print(partes)
```

### Por que usar .partition()?

O método `.partition()` é útil quando você precisa dividir uma string em exatamente três partes, com base em um separador específico. Isso pode ser útil em situações em que você precisa separar uma string em prefixo, separador e sufixo.

## Convertendo uma string em lista com .split()

Outra forma muito utilizada para converter uma string em uma lista é utilizando o método `.split()`. Este método divide a string em uma lista de substrings, com base em um delimitador especificado.

### Exemplo de uso do .split()

Vamos considerar uma string que queremos dividir em uma lista de palavras:

```python
# String de exemplo
frase = "Python é incrível"

# Convertendo a string em lista usando .split()
palavras = frase.split()

# Exibindo a lista resultante
print(palavras)
```

### Por que usar .split()?

O método `.split()` é extremamente versátil e permite que você divida uma string em uma lista de substrings com base em qualquer delimitador. Por padrão, ele usa espaços em branco, mas você pode especificar qualquer outro caractere:

```python
# Usando vírgula como delimitador
frase_com_virgula = "Python,é,incrível"
palavras_com_virgula = frase_com_virgula.split(",")
print(palavras_com_virgula)
```

## Conclusão

Agora, você já está apto a realizar manipulações de textos das básicas às mais avançadas, utilizando os diversos métodos desse tipo de dado tão utilizado. As strings são um elemento fundamental na programação Python e esperamos que este artigo tenha lhe ajudado a ter um entendimento profundo de como utilizá-las de forma eficiente.
