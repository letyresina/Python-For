'''
    Exercício 7:
    Escreva um algoritmo que exiba 20 números aleatórios sorteados entre 1 e 50 (Dica: utilize a 
    biblioteca random).
'''
from random import randint

import random;

for i in range(1 , 21):
    print("O número aleatório gerado foi: ", random.randint(0,51))
