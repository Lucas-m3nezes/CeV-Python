"""Faça um algoritmo que leia um Salarío de um funcionário e mostre seu novo salarío, com 15% de Aumento."""


salario = float(input('Digite o seu salário: R$'))
novoSalario = salario + (salario * 15/100)

print('Seu novo salário é de: R${}'.format(novoSalario))