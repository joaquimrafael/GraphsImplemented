# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 19:23:18 2023

@author: icalc
"""
from pilha import Pilha

p = Pilha()

n = int(input("Digite um numero inteiro em decimal: "))

nSalvo = n

while n != 0:
    resto = n % 2
    p.push( resto )
    n = n // 2

print(f"\nTotal de Elementos na pilha: {p.totalElementos():2d}" )

print(f"\nO correspondente binario do valor {nSalvo:2d}  e: ", end="")
		  		  
while not p.isEmpty():
    print(p.pop(), end="");
