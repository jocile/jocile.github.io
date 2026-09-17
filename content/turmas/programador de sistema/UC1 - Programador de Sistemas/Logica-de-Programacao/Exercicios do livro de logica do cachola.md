---
title: Exercícios Do Livro De Logica Do Cachola
description: 'Exercícios do livro de logica do cachola'
date: '2026-09-14'
draft: false
tags:
- exercícios
- Lógica 
---

## Exercícios do livro de logica do cachola

### Condicionais

- Crie um programa para uma loja de sucos. O preço de cada suco é R$ 5.50, porém, se o cliente comprar mais de 10 sucos, o preço individual passa para R$ 4.50. O programa deve solicitar a quantidade de sucos desejados pelo cliente e apresentar o preço final a ser pago.
- Crie um programa para gerenciar uma fila de atendimento. O programa deve perguntar se a pessoa precisa de atendimento prioritário ou não. Se for respondido "sim", o programa deve mostrar a mensagem "Vá para os caixas 1, 2 e 3". Caso contrário, o programa deve mostrar a mensagem "Vá para qualquer caixa, exceto os 1, 2 e 3, que são prioritários."
- Crie um programa para calcular e informar se compensa mais abastecer um automóvel com gasolina ou com etanol. O programa deve solicitar ao usuário o preço da gasolina e, em seguida, o preço do etanol. Depois efetuar a divisão do preço do etanol pelo preço da gasolina. Se o resultado for maior ou igual a 0.7, o programa deve apresentar a mensagem "Compensa abastecer com gasolina". Caso contrário, o programa deve apresentar a mensagem "Compensa abastecer com etanol."
- Crie um programa que solicite ao usuário um número e apresente na tela qual é o dia da semana do respectivo número. Considere que os números fornecidos devem estar no intervalo entre 1 e 7. Considere que 1 é domingo, 2 é segunda e assim por diante.
- Crie um programa para uma loja de sucos no qual são oferecidos os seguintes sucos: L - Laranja, M - Morango, A - Acerola e U - Uva. O usuário deve informar uma letra e o sistema apresentará o nome do suco e qual a principal vitamina que o suco fornece, são elas: laranja vitamina C, morango vitamina A, acerola vitamina C e uva vitamina E.
- Crie um programa que solicite ao usuário a estação do ano desejada, e o sistema deve apresentar o dia que começa a estação, são elas: outono - 20 de março, inverno - 21 junho, primavera - 22 setembro e verão - 21 de dezembro.
- Crie um programa que solicite ao usuário uma vogal e apresente palavras de acordo com a vogal informada.
- Crie um programa que solicite ao usuário um peso e uma altura, e apresente na saída o valor do IMC e um dos seguintes indicadores, são eles: IMC menor que 18.5 - magreza -, IMC entre 18.5 e 24.9 - normal, IMC entre 24.9 e 30 - sobrepeso e IMC maior que 30 - obesidade. A fórmula para o cálculo é IMC = peso / (altura * altura).
- Crie um programa que verifique se um candidato está apto a tirar a carteira de motorista do tipo D. Os requisitos são: ter idade maior que 21 anos; estar habilitado pelo menos dois anos com a carteira B ou um ano com a carteira C; não ter nenhuma infração nos últimos doze meses.
- Crie um programa para calcular o desconto de acordo com os itens comprados em uma padaria. Se o cliente comprar 10 pães e mais um queijo, ele ganha 10% de desconto. Se o cliente comprar uma bisnaga ou um pão de forma, ele tem um desconto de 15%. Agora se o cliente comprar leite e pão doce ou suspiro, ele ganha 5% de desconto. Os preços dos produtos devem ser definidos por você. O desconto não é acumulativo e será aplicado o maior percentual, de acordo com as regras, uma única vez no final da compra.
- Crie um programa para calcular a média aritmética de um aluno em um bimestre. Seu programa deve pedir a nota do teste, a nota da prova e a quantidade de faltas do aluno. Se o aluno tiver a média maior ou igual a 7.0 e menos que 10 faltas, ele estará aprovado. Se o aluno tiver média entre 5.0 e 6.9 e menos que 10 faltas, ele estará em recuperação. Se o aluno tiver média menor que 5.0 ou mais que 10 faltas, ele estará reprovado.
- Crie um programa que solicite ao usuário um número entre 1 e 12 e apresente na tela o mês correspondente.
- Crie um programa que solicite uma letra ao usuário e diga se é uma vogal ou não vogal.
- Crie um programa que solicite o tamanho de uma blusa (P, M e G) e apresente o tamanho da blusa solicitada. (P: 0.46 X 0.55 - M: 0.51 X 0.56 - G: 0.52 X 0.58)

### Repetição

- Crie um programa que solicite 5 números e apresente na tela a soma de todos os números.
- Crie um programa para ler 10 números e no final da leitura de todos os números apresente quantos números lidos foram maiores que 50.
- Crie um programa para ler a altura de 12 atletas de basquete. Apresente no final quantos têm mais de 1.90.
- Crie um programa para ler a nota de 25 alunos de uma turma de lógica de programação. Apresente no final da leitura a maior nota, a menor nota e a média das
notas.
- (Trabalhoso) Crie um programa que solicite ao usuário o número de bolinhas de gude que estão em um pote de vidro. Se o número digitado for igual a 82, apresente a mensagem "Parabéns, você acertou". Se o número digitado for menor que 82, apresente a mensagem "Você errou! Existem mais bolinhas do que você digitou". Se o número digitado for maior que 82, apresente a mensagem "Você errou! Existem menos bolinhas do que você digitou". O programa deve dar 5 oportunidades para que o usuário tente acertara quantidade correta de bolinhas de gude.

- Vamos pensar juntos: imagine que você foi contratado para desenvolver um sistema de uma clínica de vacina. Todos os dias, a clínica recebe apenas 30 vacinas BCG. Monte um programa utilizando o comando enquanto que solicite quantos dias de nascimento tem o bebê que receberá a vacina BCG. Ao atingir o limite de 30 vacinas, o programa deve mostrar a média de dias dos bebês vacinados.


```
//Exemplo 55: Algoritmo de uma clínica para vacinação de 30 (trinta) recém-nascidos com a vacina BCG.
inteiro totalDiasNascimento = 0, diasNascimento, contador = 1
enquanto (contador <= 30)
 escreva ("Digite a quantidade de dias do recém-nascido: ")
 leia (diasNascimento)
 totalDiasNascimento = totalDiasNascimento + diasNascimento
 contador++
escreva(A Média dos bebês vacinados no dia foi de: ", totalDiasNascimento/30)
```

- (Faça enquanto) Você foi contratado para desenvolver um sistema de emissão de boletos. O cliente deve informar qual o melhor dia para pagamento do boleto. Os dias disponíveis são 2, 5 ou 10. O sistema deve validar o dia informado pelo cliente e apresentar a mensagem boleto registrado caso o dia seja válido. Se o dia for inválido, o sistema deve solicitar um novo dia até que ele seja digitado corretamente.
