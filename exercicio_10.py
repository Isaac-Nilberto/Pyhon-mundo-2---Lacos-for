#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 19:28:05 2022

@author: isaacnilberto
"""
"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o
maior e o menor peso.
"""

peso = []

for pessoa in range(1,6):
    
    valor = float(input(f'Escolha da massa do {pessoa}ª individuo: '))
    peso.append(valor)
print(peso)
print("A menor massa é {} e a maior é {}".format(min(peso), max(peso)))

#%%%%

maior = 0

menor = 0
for p in range(1,6):
    
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O maior peso lido foi de {}Kg".format(maior))
print("O menor peso lido foi de {}Kg".format(menor))