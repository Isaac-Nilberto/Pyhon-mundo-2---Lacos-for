#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 19:25:48 2022

@author: isaacnilberto
"""

"""
Faça um programa que leia um número inteiro e diga se ele é primo ou não.
"""
tot = 0
numero = int(input('Digite um numero: '))
for i in range(1, numero + 1):
    if numero % i == 0:
        print('\033[33m')
        tot += 1
    else:
        print('\033[31m')
    print('{} '.format(i), end= '')
print('\n O numero {} foi divisivel {} vezes'.format(numero,tot))
if tot ==2:
    print('E primo')
else:
    print('Nao e primo')