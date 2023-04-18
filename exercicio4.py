# Importando a biblioteca math
import math

for num in range(1, 16):
    num = int(input("Informe um número: "))
    raizQuadrada = math.sqrt(num)
    print(f"{raizQuadrada:.1f}")