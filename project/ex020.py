"""O mesmo professor do desafio 019 que sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que
leia o nome dos quatro alunos e mostre a ordem sorteada."""

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))

import random
lista = [a1, a2, a3, a4]
random.shuffle(lista)

print('A ordem de apresentação será:')
print(lista)