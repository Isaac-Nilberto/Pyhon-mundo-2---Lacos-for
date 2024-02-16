#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 21:24:15 2022

@author: isaacnilberto
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares, se o valor digitado for ímpar desconsidere.
"""

lista = []


for i in range(0,5):
    valor = int(input('Escreva o valor inteiro: '))
    lista.append(valor)
print(lista)

valor = 0
for x in range(len(lista)):
    if lista[x] % 2 == 0:
        print(lista[x])
        valor = valor + lista[x]
                   
    else:
        pass
print('o valor é', valor)

#%%%%

soma = 0
cont = 0

for i in range(1,7):
    num = int(input('Digite o {} valor '.format(i)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('o valor informado é {} numeros pares e a soma foi {}'.format(cont, soma))