---
title: Exercícios De Lógica
description: 'Pratique os exercícios seguintes com o editor: Portugol Webstudio!'
date: '2026-09-14'
draft: false
tags:
- exercícios
- Lógica 
---


Pratique os exercícios seguintes com o editor: [Portugol Webstudio](https://dgadelha.github.io/Portugol-Webstudio/)!

## Exercícios aritméticos

### Comparação de números

1. Faça um algoritmo para ler dois números e imprimir a soma dos números lidos.
2. Faça um algoritmo para ler três números e imprimir a soma, média e produto dos números lidos.
3. Faça um algoritmo para ler dois números e imprimir o maior, o menor ou então dizer se são iguais.
4. Faça um algoritmo para ler um número inteiro e dizer se o número lido é par ou impar.
5. Faça um algoritmo para ler dois números A e B e dizer se A é divisível por B.
6. Faça um algoritmo para ler dois números e imprimi-los em ordem crescente.
7. Faça um algoritmo para ler três números e imprimir o maior.
8. Faça um algoritmo para ler três números e imprimir se estes podem ou não formar um triângulo.
 Observação – Para formar os lados de um triângulo cada um dos valores tem que ser menor que a soma dos outros dois.
9. Faça um algoritmo para ler três números e se estes poderem formar um triângulo dizer se o triângulo é “EQUILÁTERO”, “ISÓSCELES” OU “ESCALENO”.
10. Faça um algoritmo para ler o preço de compra de uma mercadoria e calcular o seu preço de venda para que possa ser obtido um lucro de 30%.
11. Faça um algoritmo para ler os catetos de um triângulo retângulo e calcular e imprimir a sua hipotenusa.
12. Faça um algoritmo para ler o raio e calcular o comprimento, a área e o volume de uma esfera.

|        DADOS: |              |
| ------------: | ------------ |
| Comprimento : | $P = 2\pi R$ |
|        Área : | $A = \pi R^2$ |
|       Volume: | $V = \frac 3 4 \pi R^3$ |

Resolução 1:

```c
programa calculodaesfera;
constante
pi <- 3,1416
variável
raio: real;
Inicio
    leia ( raio );
    escreva(‘O comprimento da esfera é ‘, 2 * pi * raio);
    escreva(‘A área da esfera é ‘, pi * raio ** 2 );
    escreva(‘O volume da esfera é ‘, ( 3 * ( pi * raio ** 3 ) ) / 4);
fim
```

Resolução 2:

```c
programa calculodaesfera;
constante
pi <- 3,1416
variável
raio, comp, area, vol : real;
Inicio
    escreva(‘Favor digitar o raio da esfera’);
    leia ( raio );
    comp <- 2 * pi * raio;
    area <- pi * raio ** 2;
    vol <- 3 * ( pi * raio ** 3 ) ) / 4;
    escreva(‘O comprimento da esfera é ‘, comp );
    escreva(‘A área da esfera é ‘, area );
    escreva(‘O volume da esfera é ‘, vol );
fim.
```
## Média

1. Faça um algoritmo que leia as três notas, as faltas e o nome de um aluno e imprima sua situação. ( “APROVADO”, “REPROVADO POR FALTA” ou “REPROVADO POR MÉDIA” )
  Observação – A média para aprovação é 5.0 e o limite de faltas é 17.
2. Construa um algoritmo que calcule a média aritmética entre quatro notas quaisquer fornecidas pelo usuário.

Resolução Nº1:

```c
Programa média;

variaveis
N1, N2, N3, N4: real;

inicio
leia ( N1, N2, N3, N4 );
escreva ( ( N1 + N2 + N3 + N4 ) / 4 );
fim
```

Resolução Nº2:

```c
Programa média;

variaveis
N1, N2, N3, N4, MEDIA: real;

Inicio
leia ( N1, N2, N3, N4 );
MEDIA <- ( N1 + N2 + N3 + N4 ) / 4;
Escreva ( MEDIA );  
fim
```

Resolução Nº3:

```c
Programa média;

variaveis
N1, N2, N3, N4, MEDIA: real;

inicio
leia ( N1, N2, N3, N4 );
MEDIA <- ( N1 + N2 + N3 + N4 ) / 4;
Escreva ( “A media aritmética do aluno nas quatro notas tiradas é “, MEDIA );  
fim
```

### Média das médias

Faça um algoritmo para ler nove número inteiros quaisquer. Tirar a média aritmética dos três primeiros, depois a média dos outros três e por fim a média dos três últimos. Escreva as três médias e a média das três médias.

Resolução Nº1:

```c
programa médiadasmédias;

variáveis
N1, N2, N3, N4, N5, N6, N7, N8, N9: inteiro;

Inicio

leia ( N1, N2, N3, N4, N5, N6, N7, N8, N9 );
escreva(“A media dos primeiro três números é “, ( N1 + N2 + N3 ) / 3);
escreva(“A media dos outros três números é , ( N4 + N5 + N6 ) / 3);
escreva(“A media dos últimos três números é “, ( N7 + N8 + N9 ) / 3);
escreva(“Media das medias “,((N1 + N2 + N3) / 3 + (N4 + N5 + N6) / 3 + (N7 + N8 + N9) / 3) / 3);
fim
```

Resolução Nº2:

```c
programa médiadasmédias;

variáveis
N1, N2, N3, N4, N5, N6, N7, N8, N9: inteiro;
MEDIA1, MEDIA2, MEDIA3: real; 

inicio
leia ( N1, N2, N3, N4, N5, N6, N7, N8, N9 );
MEDIA1 <- ( N1 + N2 + N3 ) / 3;
MEDIA2 <- ( N4 + N5 + N6 ) / 3;
MEDIA3 <- ( N7 + N8 + N9 ) / 3;
escreva(“A media dos primeiro três números é “, MEDIA1);
escreva(“A media dos outros três números é “, MEDIA2;
escreva(“A media dos últimos três números é “, MEDIA3);
escreva(“A media das medias é “,(MEDIA1 + MEDIA2 + MEDIA3) / 3);
fim
```

Resolução Nº3:

```c
programa médiadasmédias;

variáveis
N1, N2, N3, N4, N5, N6, N7, N8, N9: inteiro;
MEDIA1, MEDIA2, MEDIA3, MMEDIA: real; 

inicio
leia ( N1, N2, N3, N4, N5, N6, N7, N8, N9 );
MEDIA1 <- ( N1 + N2 + N3 ) / 3;
MEDIA2 <- ( N4 + N5 + N6 ) / 3;
MEDIA3 <- ( N7 + N8 + N9 ) / 3;
MMEDIA <- ( MEDIA1 + MEDIA2 + MEDIA3 ) / 3;
escreva(“A media dos primeiro três números e “, MEDIA1);
escreva(“A media dos outros três números e “, MEDIA2);
escreva(“A media dos últimos três números e “, MEDIA3);
escreva(“A media das medias e “,MMEDIA);
fim
```

## Peso ideal

Faça um algoritmo para calcular o peso ideal de uma pessoa sabendo sua altura.\
DADO: 

- para homens ( 72,7 * altura ) – 58;
- para mulheres ( 62,1 * altura ) – 44,7.

Resolução Nº1:

```c
programa pesoideal;

variável
ALT: real;

inicio

leia ( ALT );
escreva(“Se a altura lida for de um homem seu peso ideal será de “, ( 72,7 * ALT ) – 58 ),“Kg);
escreva(“Se a altura lida for de uma mulher seu peso ideal será de“,(62,1 * ALT) – 44,7), “Kg”);

fim
```

Resolução Nº2:

```c
programa pesoideal;

variáveis
ALT, ALTH, ALTM: real;

Inicio

leia ( ALT );
ALTH <- ( 72,7 * ALT ) – 58;
ALTM <- ( 62,1 * ALT ) – 44,7;
escreva(“Se a altura lida for de um homem seu peso ideal será de “, ALTH, “Kg”);
escreva(“Se a altura lida for de uma mulher seu peso ideal será de “, ALTM, “Kg”);

fim
```

## Manipulando textos

Faça um algoritmo para ler duas variáveis caractere e concatená-las em uma terceira.

```c
programa concatenar;
variável
palavra1, palavra2, conca  : caracter ;
Inicio
    escreva(‘Favor digitar as duas palavras’);
    leia ( palavra1, palavra2 );
    conca  <-  palavra1 + palavra2 ;
    escreva(‘As duas palavras são’, palavra1 , ‘  e ‘, palavra2 );
    escreva(‘A concatenação das duas palavras é’ , conca );
fim.
```

Faça um algoritmo para ler duas variáveis inteiras e trocar o conteúdo lido de uma pela outra.

```c
programa trocanumero;
variável
n1, n2, aux  : inteiro ;
Inicio
    escreva(‘Favor digitar os dois numeros’);
    leia ( n1, n2 );
    aux <- n2 ;
    n2 <- n1 ;
    n1 <- aux;
fim.
```

#programador/algoritmos 
