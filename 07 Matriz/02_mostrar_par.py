import os

matriz = []
tot_par = 0


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


for l in range(3):
    matriz.append([l, l, l])

for l in range(3):
    for c in range(3):
        r = int(input(f"Digite o valor da posição [{l}]{c}] "))
        matriz[l][c] = r

limpar_tela()

for l in range(3):
    for c in range(3):
        if matriz[l][c] % 2 == 0:
            tot_par += 1
            print(f" [{matriz[l][c]}]", end="  ")
        else:
            print(" ", matriz[l][c], end="   ")
    print()

print(f"\nAo todo foram exibidos {tot_par} numeros pares ")
