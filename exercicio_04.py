#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 21:44:47 2022

@author: isaacnilberto
"""
'''
Mostre o valor do número da tabuada que o usuário escolher utilizando o laço for.
'''

valor = int(input('Escolha o valor que queres saber a tabuada: '))
print('='*30)
for i in range(0,11):
    print(f'O {valor} * {i} é igual a {valor * i}' )
    
#%%%%%%%%

num = int(input('Escolha o valor que queres saber a tabuada: '))

for c in range(1,11):
    print('{} x {:2} = {}'.format(num, c, num*c))