import os

matriz = []

for i in range(3):
    matriz.append([i, i, i])


for linha in range(3):
    for coluna in range(3):
        p = int(input("Valor: "))
        matriz[linha][coluna] = p

os.system("clear")
for i in range(3):
    for j in range(3):
        print(matriz[i][j], end="  ")
    print()
