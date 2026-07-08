import os, random

matriz = []


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def menu():
    print("""
MENU OPÇÕES
======================
[1] Mostrar a Matriz
[2] Diagonal Principal
[3] Triangulo Superior
[4] Triangulo Inferior
[5] Sair
======= OPÇÃO: """)


for i in range(4):
    linha = []
    for j in range(4):
        linha.append(random.randint(1, 50))
    matriz.append(linha)


while True:
    menu()

    try:
        op = int(input(" "))
        limpar_tela()

        match op:

            case 1:
                for i in matriz:
                    for j in i:
                        print(f"{j:>3}", end=" ")

                    print()
            case 2:
                for l in range(4):
                    for c in range(4):
                        if l == c:
                            print(f"{matriz[l][c]:>4}", end="")
                        else:
                            print(" " * 4, end="")
                    print()
            case 3:
                for l in range(4):
                    for c in range(4):
                        if l == c or c == 0 or l == 3:
                            print(" " * 4, end="")
                        elif l == 2 and c == 1:
                            print(" " * 4, end="")
                        else:
                            print(f"{matriz[l][c]:>4}", end="")
                    print()
            case 4:
                for l in range(4):
                    for c in range(4):
                        if l == c or l == 0 or c == 3:
                            print(" " * 4, end="")
                        elif l == 1 and c == 2:
                            print(" " * 4, end="")
                        else:
                            print(f"{matriz[l][c]:<4}", end="")
                    print()

            case 5:
                break

            case _:
                print("ERRO: OPÇÃO INVALIDA")
    except ValueError:
        print("ERRO:  DIGITE APENAS NUMERO")
