---
title: "dataclasses"
date: 2026-09-23
draft: false
tags:
  - Python/POO
  - dataclasses
description: "contêineres de dados, com atributos e métodos padrão gerados automaticamente."
---

## Explicando DataClass em Python

As DataClasses são uma funcionalidade introduzida no Python 3.7 que simplificam a criação de classes simples de dados. Elas fornecem uma maneira concisa e elegante de definir classes que são essencialmente contêineres de dados, com atributos e métodos padrão gerados automaticamente.

### Benefícios das DataClasses

1. **Código mais conciso**: As DataClasses reduzem significativamente a quantidade de código necessária para criar uma classe simples de dados, poupando tempo e esforço do desenvolvedor.
2. **Geração automática de métodos**: As DataClasses geram automaticamente métodos comuns, como `__init__()`, `__repr__()`, `__eq__()`, `__hash__()` e `__str__()`, eliminando a necessidade de escrevê-los manualmente.
3. **Validação de dados**: As DataClasses permitem a definição de tipos de dados para os atributos, o que facilita a validação e a manutenção da integridade dos dados.
4. **Imutabilidade**: As DataClasses podem ser definidas como imutáveis, o que as torna adequadas para uso em estruturas de dados imutáveis, como tuplas e conjuntos.

### Criando uma DataClass

Para criar uma DataClass, você pode usar o decorador `@dataclass` fornecido pelo módulo `dataclasses` do Python. Aqui está um exemplo:

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str
```

Neste exemplo, a classe `Person` é definida como uma DataClass com três atributos: `name`, `age` e `email`. O decorador `@dataclass` gera automaticamente os métodos padrão, como `__init__()`, `__repr__()` e `__eq__()`.

### Usando uma DataClass

Agora que temos a classe `Person` definida, podemos usá-la da seguinte maneira:

```python
person = Person(name="John Doe", age=35, email="john.doe@example.com")
print(person)  # Output: Person(name='John Doe', age=35, email='john.doe@example.com')
print(person.name)  # Output: John Doe
print(person.age)  # Output: 35
print(person.email)  # Output: john.doe@example.com
```

Observe que não precisamos definir manualmente o método `__init__()` ou qualquer outro método padrão. Eles são gerados automaticamente pela DataClass.

### Personalização das DataClasses

As DataClasses oferecem várias opções de personalização, como:

- Definir valores padrão para os atributos
- Marcar atributos como opcionais
- Adicionar métodos personalizados
- Herdar de outras classes
- E muito mais

Você pode encontrar mais informações sobre essas e outras funcionalidades na [documentação oficial do Python sobre DataClasses](https://docs.python.org/3/library/dataclasses.html).

Em resumo, as DataClasses são uma adição poderosa e conveniente ao Python, simplificando a criação de classes simples de dados e reduzindo a quantidade de código necessária. Elas são uma ferramenta útil para qualquer desenvolvedor Python que trabalhe com estruturas de dados.
