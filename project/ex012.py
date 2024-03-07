"""Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de Desconto."""


preco = int(input('Digite o preço do produto: '))
novoPreco = preco - (preco * 5/100)

print('O novo preço do produto é', novoPreco)