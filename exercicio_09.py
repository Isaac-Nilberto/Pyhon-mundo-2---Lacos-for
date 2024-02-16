#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 20:18:44 2022

@author: isaacnilberto
"""

"""
Crie um programa que leia o ano de nascimento e sete pessoas. No final, mostre quantas
pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

from datetime import date

lista_idade = []
atual = date.today().year

for idade in range(0,7):
    valor = int(input("Qual idade de nascimento em anos? "))
    lista_idade.append(valor)
print("O conjunto de anos de nascimento é ")

menor_idade = 0

maior_idade = 0


for i in range(len(lista_idade)):
    if atual - lista_idade[i] < 18:
        menor_idade += 1
    else:
        maior_idade += 1
print("A quantidade de pessoas menores de idade é {} e maiores de idade {}".format(menor_idade,maior_idade))

#%%%
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0

for pessoa in range(1,8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu?'.format(pessoa)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1

print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('Ao todo tivemos {} pessoas menores de idade'.format(totmenor))

        
    