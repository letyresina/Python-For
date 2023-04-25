'''
    Exercício 4:
    Escreva um algoritmo que leia quinze números informados pelo usuário e exiba a raiz quadrada 
    de cada número (Dica: utilize a biblioteca math)
'''
# Importando a biblioteca math
import math

for num in range(1, 16):
    num = int(input("Informe um número: "))
    raizQuadrada = math.sqrt(num)
    print(f"{raizQuadrada:.1f}")