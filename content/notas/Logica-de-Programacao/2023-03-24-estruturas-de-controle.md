---
title: 2023 03 24 Estruturas De Controle
description: Permite a escolha de um grupo de ações e estruturas a ser executado quando
  determinadas condições, representadas por expressões lógicas, são ou não satisfeitas.
date: '2026-09-14'
draft: false
tags:
- exercícios
- lógica
- programador
- programação
- senac
---

Permite a escolha de um grupo de ações e estruturas a ser executado quando determinadas condições, representadas por expressões lógicas, são ou não satisfeitas.

```code
SIMPLES ( SE /  ENTÃO  /  INICIO  /  FIM )
		| nome do programa
		|
		| declaração de variáveis
		|
   		inicio
		| 
		|     se < condição > entao;
        |     inicio
        |             comando a;
		|	           .
		|             comando n;
		|     fim;
		|          .
		|          .
		|     comando x;
		fim.

```

## Condição

É uma expressão lógica que, quando inspecionada, pode gerar um resultado falso ou verdadeiro. Se < condição > for verdadeira a cláusula que está entre o "início do se" e o "fim do se" será executada. Se < condição > for falsa a cláusula que está entre o "início do se" e o "fim do se" não será executada.

## Exercícios

1. Faça um algoritmo para ler dois números e imprimir o maior, o menor ou então dizer se são iguais.
2. Faça um algoritmo para ler um número inteiro e dizer se o número lido é par ou impar.
3. Faça um algoritmo para ler dois números A e B e dizer se A é divisível por B.
4. Faça um algoritmo para ler dois números e imprimi-los em ordem crescente.
5. Faça um algoritmo para ler três números e imprimir o maior.

DESAFIO

01- Faça um algoritmo para ler três números e imprimir se estes podem ou não formar um triângulo.

Observação - Para formar os lados de um triângulo cada um dos valores tem que ser menor que a soma dos outros dois.

02- Faça um algoritmo para ler três números e se estes poderem formar um triângulo dizer se o triângulo é "EQUILÁTERO", "ISÓCELES" OU "ESCALENO".

03- Faça um algoritmo que leia as três notas, as faltas e o nome de um aluno e imprima sua situação. ( "APROVADO", "REPROVADO POR FALTA" ou "REPROVADO POR MÉDIA" )

Observação - A média para aprovação é 5.0 e o limite de faltas é 17.

## Exemplos

Teste se um valor digitado é positivo ou não:

```code
programa seleção_simples;

variáveis
valor: real;
inicio
    escreva(´digite um valor negativo´);
    leia ( valor );
    se valor > 0 entao; 
         inicio
             escreva(´foi digitado um valor positivo´);
         fim ;
    se valor < 0 entao; 
         inicio
             escreva(´foi digitado um valor negativo´);
         fim; 
fim.

```

MELHORAR O ALGORITMO.

```code
programa seleção_simples;
variáveis
valor: real;
inicio
    escreva(´digite um valor negativo´);
    leia ( valor );
    se valor > 0 entao; 
         inicio
             escreva(´foi digitado um valor positivo que vale´, valor);
         fim ;
     se valor = 0 entao; 
         inicio
             escreva(´foi digitado o valor zero´);
         fim ;
    se valor < 0 entao; 
         inicio
             escreva(´foi digitado um valor negativo que vale´, valor);
         fim; 
fim.

```

Exercício para sala de aula

Fazer o exercício do peso ideal testando uma altura válida.

```code
programa pesoideal;

variáveis
ALT, PESOIDH, PESOIDM: real;
inicio
    escreva( ´digite uma altura´);
    leia ( ALT );
    se ALT <= 2.50 e ALT >= 0.60 entao;
         inicio
              PESOIDH = ( 72.7 * ALT ) - 58;
              PESOIDM = ( 62.1 * ALT ) - 44.7;
              escreva(´Se a altura for de um homem seu peso ideal e ´, PESOIDH, "Kg");
              escreva(´Se a altura for de uma mulher seu peso ideal e ´, PESOIDM, "Kg");
         fim; 
    se ALT > 2.50 ou ALT < 0.60 entao;
         inicio
              escreva( ´Altura invalida´);
         fim;
fim.

```

## Exemplo de situação do aluno em Pascal

```pascal
Program situacao_aluno;
var
      nt1, nt2, nt3, media : real;
      faltas : integer;
      nome : string ;
begin
      writel'DIGITE O NOME DO ALUNO: ');
      readIn(nome); 
      writel'DIGITE AGORA SUA 1ª NOTA: ');
      readIn(nt1); 
      writel'DIGITE AGORA SUA 2ª NOTA: ');
      readIn(nt2); 
      writel'DIGITE AGORA SUA 3ª NOTA: ');
      readIn(nt3); 
      writel'DIGITE AGORA SUAS FALTAS: ');
      readIn(faltas); 
      if (nt1 >= 0) and (nt1<=10 ) and (nt2 >= 0) and (nt2<=10) and  (nt3 >= 0) and (nt3<=10 ) then
         begin
              if  faltas >= 0 then
                  begin
                      media := ( nt1 + nt2 + nt3 ) / 3;
                      if ( media >= 5 ) and ( faltas <= 17 ) then 
                          begin
                              writeln('O aluno ´, nome, ´está aprovado com média de ´, media );
                          end
                      else
                          if media < 5 then 
                             begin
                                 writeln('O aluno ´, nome, ´está reprovado por média com média de ´, media );
                             end
                          else
                             begin
                                 writeln('O aluno ´, nome, ´está reprovado por falta com ´, faltas, ´ faltas. );
                             end
              else
                  begin
                       writeln('NÃO EXISTE NÚMERO DE FALTAS NEGATIVO');
                  end
      else
         begin
             writeln('AS NOTAS TEM QUE ESTAR ENTRE ZERO E DEZ');
         end;
end.

```

## Referências

- [Portugol Webstudio editor online](https://dgadelha.github.io/Portugol-Webstudio/)
