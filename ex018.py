"""Faça um programa que leia o ângulo e mostre na tela o valor do seno, cosseno e tangente desse ângulo."""


import math

angulo = float(input('Digite o ângulo que você deseja: '))
radianos = math.radians(angulo)

se = math.sin(radianos)
co = math.cos(radianos)
ta = math.tan(radianos)

print(f'O ângulo de {angulo} graus tem o SENO de {se:.2f}')
print(f'O ângulo de {angulo} graus tem o COSSENO de {co:.2f}')
print(f'O ângulo de {angulo} graus tem a TANGENTE de {ta:.2f}')