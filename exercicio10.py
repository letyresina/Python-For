'''
    Exercício 10:
    Escreva um algoritmo que determine se um número N (digitado pelo usuário) é primo ou não.
'''

N = int(input("Informe um número inteiro qualquer: "))
multiplo = 0

for i in range(2, N):
    if (N % i == 0):
        multiplo += 1

if (multiplo == 0 and N != 1):
    print(f"O número {N} é primo")
else:
    print(f"O número {N} não é primo")