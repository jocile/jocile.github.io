---
title: Exercícios De Lógica Aritmética
description: criando algoritmos para programas de computador resolvendo problemas
date: '2026-09-14'
draft: false
tags:
- exercícios
- Lógica 
---

Resolva os exercícios usando a linguagem Portugol ou VisuAlg.

1. Construa um algoritmo que calcule a média aritmética entre quatro notas quaisquer fornecidas pelo usuário.
2. Faça um algoritmo para ler nove número inteiros quaisquer. Tirar a média aritmética dos três primeiros, depois a média dos outros três e por fim a média dos três últimos. Escreva as três médias e a média das três médias.
3. Faça um algoritmo para calcular o peso ideal de uma pessoa sabendo sua altura.
4. Faça um algoritmo para ler o raio e calcular o comprimento, a área e o volume de uma esfera. DADOS: comprimento = P = 2πR; área da superfície = A = 4πR^2; volume = V = (4/3) πR^3;
5. Faça um algoritmo para ler duas variáveis caracter e concatená-las em uma terceira.
6. Faça um algoritmo para ler duas variáveis inteiras e trocar o conteúdo lido de uma pela outra.

Resoluções sugeridas a seguir:

## Média aritmética

Construa um algoritmo que calcule a média aritmética entre quatro notas quaisquer fornecidas pelo usuário.

Resolução Nº1

```code
Programa média;
variaveis
N1, N2, N3, N4: real;
inicio
leia ( N1, N2, N3, N4 );
escreva ( ( N1 + N2 + N3 + N4 ) / 4 );
fim
```

Resolução Nº2

```script
Programa média;

variaveis
N1, N2, N3, N4, MEDIA: real;

Inicio
leia ( N1, N2, N3, N4 );
MEDIA = ( N1 + N2 + N3 + N4 ) / 4;
Escreva ( MEDIA );
fim
```

Resolução Nº3

```script
Programa média;

variaveis
N1, N2, N3, N4, MEDIA: real;

inicio
leia ( N1, N2, N3, N4 );
MEDIA = ( N1 + N2 + N3 + N4 ) / 4;
Escreva ( "A media aritmética do aluno nas quatro notas tiradas é ", MEDIA );
fim
```

Desafio

- Faça um algoritmo para ler nove número inteiros quaisquer. Tirar a média aritmética dos três primeiros, depois a média dos outros três e por fim a média dos três últimos. Escreva as três médias e a média das três médias.

Resolução Nº1

```code
programa médiadasmédias;

variáveis
N1, N2, N3, N4, N5, N6, N7, N8, N9: inteiro;

Inicio

leia ( N1, N2, N3, N4, N5, N6, N7, N8, N9 );
escreva("A media dos primeiro três números é ", ( N1 + N2 + N3 ) / 3);
escreva("A media dos outros três números é, ( N4 + N5 + N6 ) / 3);
escreva("A media dos últimos três números é ", ( N7 + N8 + N9 ) / 3);
escreva("Media das medias ",((N1 + N2 + N3) / 3 + (N4 + N5 + N6) / 3 + (N7 + N8 + N9) / 3) / 3);
fim

```

Resolução Nº2

```code
programa médiadasmédias;

variáveis
N1, N2, N3, N4, N5, N6, N7, N8, N9: inteiro;
MEDIA1, MEDIA2, MEDIA3: real; 

inicio
leia ( N1, N2, N3, N4, N5, N6, N7, N8, N9 );
MEDIA1 =( N1 + N2 + N3 ) / 3;
MEDIA2 =( N4 + N5 + N6 ) / 3;
MEDIA3 =( N7 + N8 + N9 ) / 3;
escreva("A media dos primeiro três números é ", MEDIA1);
escreva("A media dos outros três números é ", MEDIA2;
escreva("A media dos últimos três números é ", MEDIA3);
escreva("A media das medias é ",(MEDIA1 + MEDIA2 + MEDIA3) / 3);
fim

```

Resolução Nº3

```typescript
programa médiadasmédias;

variáveis
N1, N2, N3, N4, N5, N6, N7, N8, N9: inteiro;
MEDIA1, MEDIA2, MEDIA3, MMEDIA: real; 

inicio
leia ( N1, N2, N3, N4, N5, N6, N7, N8, N9 );
MEDIA1 =( N1 + N2 + N3 ) / 3;
MEDIA2 =( N4 + N5 + N6 ) / 3;
MEDIA3 =( N7 + N8 + N9 ) / 3;
MMEDIA =( MEDIA1 + MEDIA2 + MEDIA3 ) / 3;
escreva("A media dos primeiro três números e ", MEDIA1);
escreva("A media dos outros três números e ", MEDIA2);
escreva("A media dos últimos três números e ", MEDIA3);
escreva("A media das medias e ",MMEDIA);
fim

```

## Peso ideal

Faça um algoritmo para calcular o peso ideal de uma pessoa sabendo sua altura.

DADOS:

- para homens ( 72,7 * altura ) = 58;
- para mulheres ( 62,1 * altura ) = 44,7.

Resolução Nº1

```script
programa pesoideal;

variável
ALT: real;

inicio

leia ( ALT );
escreva("Se a altura lida for de um homem seu peso ideal será de ", ( 72,7 * ALT ) - 58 ),"Kg);
escreva("Se a altura lida for de uma mulher seu peso ideal será de",(62,1 * ALT) - 44,7), "Kg");

fim
```

Resolução Nº2

```script
programa pesoideal;

variáveis
ALT, ALTH, ALTM: real;

Inicio

leia ( ALT );
ALTH = ( 72,7 * ALT ) - 58;
ALTM = ( 62,1 * ALT ) - 44,7;
escreva("Se a altura lida for de um homem seu peso ideal será de ", ALTH, "Kg");
escreva("Se a altura lida for de uma mulher seu peso ideal será de ", ALTM, "Kg");

fim
```

## Cálculo de esfera

Faça um algoritmo para ler o raio e calcular o comprimento, a área e o volume de uma esfera.

DADOS:

- comprimento = P = 2πR
- área = A = πR2
- volume = V = πR3

Resolução Nº1

```code
programa calculodaesfera;
constante
pi = 3,1416
variável
raio: real;
Inicio
 leia ( raio );
 escreva("O comprimento da esfera é ", 2 * pi * raio);
 escreva("A área da esfera é ", pi * raio ** 2 );
 escreva("O volume da esfera é ", ( 3 * ( pi * raio ** 3 ) ) / 4);
fim
```

Resolução Nº2

```code
programa calculodaesfera;
constante
pi = 3,1416
variável
raio, comp, area, vol: real;
Inicio
 escreva("Favor digitar o raio da esfera");
 leia ( raio );
 comp = 2 * pi * raio;
 area = pi * raio ** 2;
 vol = ( 3 * ( pi * raio ** 3 ) ) / 4;
 escreva("O comprimento da esfera é ", comp );
 escreva("A área da esfera é ", area );
 escreva("O volume da esfera é ", vol );
fim.
```

## Trocas de valores

Faça um algoritmo para ler duas variáveis caracter e concatená-las em uma terceira.

```code
programa concatenar;
variável
palavra1, palavra2, conca: caracter;
Inicio
 escreva("Favor digitar as duas palavras");
 leia ( palavra1, palavra2 );
 conca = palavra1 + palavra2;
 escreva("As duas palavras são", palavra1, " e ", palavra2 );
 escreva("A concatenação das duas palavras é", conca );
fim.

```

Faça um algoritmo para ler duas variáveis inteiras e trocar o conteúdo lido de uma pela outra.

```code
programa trocanumero;
variável
n1, n2, aux: inteiro;
Inicio
 escreva("Favor digitar os dois numeros");
 leia ( n1, n2 );
 aux = n2;
 n2 = n1;
 n1 = aux;
fim.

```

## Referências

- [Programação em blocos com code.org](https://studio.code.org/s/express-2021)
- [Programação em blocos com Scratch](https://scratch.mit.edu/)
- [Portugol Webstudio editor online](https://dgadelha.github.io/Portugol-Webstudio/)
- [Resolução no Google Colab](https://colab.research.google.com/drive/1UfD8tLOFLZp3ITW_qrpN1bw-2tLN0VRh?usp=sharing)
- [[Exercícios de Logica condicional solucao]]
