menor = None;
maior = None;
i = 1;

for i in range(10):
    num = int(input("Informe um número inteiro: "))
    if menor is None or num < menor:
        menor = num
    if maior is None or num > maior:
        maior = num

print(f"O menor número foi {menor} e o maior número foi {maior}")