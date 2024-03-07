"""Um professor que sortear um dos seus quatro alunos para apaga o quadro. Faça um programa que ajude ele, lendo o nome
deles e escrevendo o nome do escolhido."""

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

import random
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)

print(f'O aluno escolhido foi {escolhido}!')
