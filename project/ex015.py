"""Escreva um programa que pergunte a quantidade de Km percorrido por um carro alugado e a quantidade de dias pelos
quais foi alugado e calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado."""


precoCarro = 60.0
diariaCarro = 0.15

dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))

valorFinal = (dias * precoCarro) + (km * diariaCarro)

print(f'O total a pagar é de R${valorFinal:.2f}.')
