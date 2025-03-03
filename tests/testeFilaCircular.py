# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 19:54:57 2023

@author: icalc
"""
from filaCircular import FilaCircular

F = FilaCircular()
n1 = int(input("Digite um nro: "))
n2 = int(input("Digite outro nro: "))

n1Aux = n1
n2Aux = n2

print(f"\nTamanho da Fila Início: {F.totalElementos():2d}.")

while n1Aux >=1:
    if n1Aux % 2 == 1:
        F.enqueue(n2Aux)
    n1Aux = n1Aux // 2
    n2Aux = n2Aux  * 2
    
print(f"Tamanho da Fila: {F.totalElementos():2d}.")

valor = 0
while not F.isEmpty():
    v = F.dequeue()
    valor = v + valor

print(f"\nO produto de {n1:2d} por {n2:2d} = {valor:2d} .\n")