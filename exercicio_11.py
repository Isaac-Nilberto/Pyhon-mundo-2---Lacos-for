#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 13:36:32 2023

@author: isaacnilberto
"""
"""
Faça um programa que leia o nome, idade e sexo de 4 pessoas. No final, 
mostre: a media de idade do grupo, qual é o nome do homem mais velho, 
quantas mulheres tem menos de 20 anos.
"""
#%%% minha solução

media_idade = 0
nome_homem_velho = 0
idade_homem_velho = ''
total_mulheres_20 = 0

for indice in range(1,5):
    print(f'------- {indice}ª pessoa -------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    
    media_idade += idade / 4
    
    if indice == 1 and sexo in 'Mm':
        nome_homem_velho = nome
        idade_homem_velho = idade
    if sexo in 'Mm' and idade > idade_homem_velho:
        nome_homem_velho = nome
        idade_homem_velho = idade
    if sexo in 'Ff' and idade < 20:
        total_mulheres_20 += 1
    
print(f'A media das idades é: {media_idade};')
print(f'O homem mais velho no grupo é {nome_homem_velho} e possui {idade_homem_velho};')
print(f'O total de mulheres menor que 20 anos é {total_mulheres_20}.')