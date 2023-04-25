'''
    Exercício 9:
    Escreva um algoritmo que solicite um número inteiro e exiba todos os divisores desse número.
'''

num = int(input("Informe um número inteiro qualquer: "))

for n in range(1, num+1):
    if num % n == 0:
        print(f"O número {n} é divisor de {num}")