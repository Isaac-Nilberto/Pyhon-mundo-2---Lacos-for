#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 21:56:04 2022

@author: isaacnilberto
"""

"""
Desenvolva um programa que leia o primeiro termo e a razão de uma P.A. No final,
mostre os 10 primeiros termos dessa progressão
"""

a1 = int(input("Entre com o primeiro termo da Progressao Aritmetica: "))
print("O valor do primeiro termo é: ", a1)
r = int(input("Entre com o valor da razão: "))
print("O valor da razão é: ", r)
n = a1 + (10-1)*r
for i in range(a1,n + r, r):
    print(i)
#%%%%%%

