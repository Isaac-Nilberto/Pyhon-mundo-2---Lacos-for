#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 19:49:32 2022

@author: isaacnilberto
"""

'''
Exercício 01:
Faça um programa que mostre na tela um contagem regressiva para o estouro de fogos
de artifício, indo de 10 até 0, com uma pausa de um segundo entre eles.
'''

import time
for x in range(10,-1,-1):
    time.sleep(1)
    print(x)
print('Fogos de artifício')