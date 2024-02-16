#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 20:02:49 2022

@author: isaacnilberto
"""

'''
Exercício 03:
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos
de três que se encontram no intervalo de 1 até 500.
'''
s = 0
c = 0
for i in range(0,500):
    if i % 2 == 0:
        pass
    else:
        if  i % 3 == 0:
            s = s + i
            c = c + 1
            print('a soma de todos os {} valores solicitados é {}'.format(s, c))
print('A soma dos múltiplos de 3 é', s)            
#%%
soma = 0
cont = 0
for i in range(1,501,2):
    if i % 3 ==0:
        cont = cont + 1
        soma = soma + i
        print('a soma de todos os {} valores solicitados é {}'.format(cont, soma))