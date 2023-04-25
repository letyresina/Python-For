'''
    Exercício 10:
    Escreva um algoritmo que determine se um número N (digitado pelo usuário) é primo ou não.
'''

N = int(input("Informe um número inteiro qualquer: "))
multiplo = 0

for i in (2, N + 1):
    if (N % i == 0):
        multiplo += 1

if (multiplo == 0):
    print(f"O número {N} é primo")
else:
    print(f"O número {N} não é primo")