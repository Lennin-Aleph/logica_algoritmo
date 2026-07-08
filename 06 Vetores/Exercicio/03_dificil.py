# Nível dificil

import os, time

produtos = []
m = "".center(50, "=")


def menu():

    os.system("cls" if os.name == "nt" else "clear")
    print(m)
    print("|", "SISTEMA DE PRODUTOS".center(46), "|")
    print(m)
    print("| [1] Cadastrar Produto                          |")
    print("| [2] Remover Produto                            |")
    print("| [3] Listar Estoque de Produto                  |")
    print("| [0] Sair                                       |")
    print(m)


def cadastrar_produto():
    produto = input("Nome do produto: ").title()

    if produto in produtos:
        print("Xx! PRODUTO JÁ CADASTRADO !xX")
    else:
        produtos.append(produto)
        print(f"{produto} foi cadastrado com sucesso", flush=True)
    time.sleep(2.5)


def remover_produto():
    produto = input("Nome do produto: ").title()

    if produto in produtos:
        produtos.remove(produto)
        print(f"{produto} foi removido com sucesso!", flush=True)
    else:
        print("Xx! PRODUTO NÃO ENCONTRADO !xX")
    time.sleep(2.5)


def listar_produtos():
    print(m)
    print("PRODUTOS CADASTRADOS:")

    if not produtos:
        print("Xx! Nenhum produto foi cadastrado ainda !xX")
        time.sleep(2.5)

    for i, produto in enumerate(produtos, start=1):
        print(f"{i}. {produto}")


while True:
    menu()
    try:
        op = int(input("Escolha uma das opções: "))

        if op == 1:
            cadastrar_produto()

        elif op == 2:
            remover_produto()

        elif op == 3:
            listar_produtos()
            print("""
    DIGITE UMA OPÇÃO:
    [V] Voltar
    [C] Cadastrar novo produto
    [R] Remover um produto
        """)

            sair = input(" ").upper()

            if sair == "C":
                menu()
                cadastrar_produto()
            elif sair == "R":
                menu()
                remover_produto()
            elif sair == "V":
                menu()
            else:
                print("Xx! OPÇÃO INVALIDA !xX")
                time.sleep(2.5)

        elif op == 0:
            print("Encerrando...")
            break

        else:
            print("Xx! OPÇÃO INVALIDA !xX")
            time.sleep(2.5)

    except:
        print("Xx! Digite apenas numeros !xX")
        time.sleep(2.5)
