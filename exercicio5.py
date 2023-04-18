quantidadeAlunos = int(input("Informe a quantidade de alunos: "))
quantidadeNotas = int(input("Informe a quantidade de nota de cada aluno "))

for i in range(quantidadeAlunos):
    somaNota = 0
    for i2 in range(quantidadeNotas):
        nota = int(input("Informe a nota do aluno: "))
        somaNota += nota
    media = somaNota / quantidadeNotas
    print(f"A média desse aluno é de {media}")