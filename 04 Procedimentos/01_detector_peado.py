# Detector de Pesado
import os

maior_p = 0
nome = ""


def cabecalho():
    os.system("clear")
    m = "".center(30, "=")
    print(m)
    print("DETECTOR DE PESADO".center(30))
    print(f"Maior peso até agora: {maior_p} Kg")
    print(m)


for i in range(1, 6):
    # os.system("clear")
    cabecalho()
    n = input("Digite o nome: ")
    peso = float(input(f"Digite o peso de {n}: "))

    if peso > maior_p:
        maior_p = peso
        nome = n

cabecalho()
print(f"A pessoa mais pesada foi {nome.title()} com {maior_p:.2f} Kg")
