N = int(input("Informe um número inteiro maior que 0: "))
resultado = 1

for n in range (1, N + 1):
    resultado *= n

print(f"O fatorial de {N}! é de {resultado}")