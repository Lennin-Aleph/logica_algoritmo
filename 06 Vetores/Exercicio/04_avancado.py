import os, time

estoque = []


def menu():
    print("""============== ESTOQUE ==============

1 - Cadastrar Produto
2 - Remover Produto
3 - Alterar Produto
4 - Procurar Produto
5 - Listar Produtos
6 - Quantidade de Produtos
7 - Limpar Estoque
0 - Sair          
=====================================""")


def tempo(t):
    time.sleep(t)


def pausa():
    input("\n Pressione ENTER para continuar ")


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def cadastrar_produto():
    produto = input("Nome do produto: ").title()

    if produto in estoque:
        print("!ERRO: PRODUTO JA CADASTRADO")
    else:
        estoque.append(produto)
        print(f"{produto} foi cadastrado com sucesso")


def remover_produto():
    produto = input("Nome do produto: ").title()

    if produto in estoque:
        estoque.remove(produto)
        print(f"{produto} foi removido com sucesso")
    else:
        print("!ERRO: PRODUTO NÃO ENCONTRADO")


def alterar_produto():
    antigo_p = input("Alterar produto: ").title()

    if antigo_p in estoque:
        novo_p = input("Novo produto: ").title()

        if novo_p in estoque:
            print("!ERRO: PRODUTO JA CADASTRADO")
        else:
            i = estoque.index(antigo_p)
            estoque[i] = novo_p
            print(f"{antigo_p} foi alterado para {novo_p} com sucesso")
    else:
        print("!ERRO: PRODUTO NÃO ENCONTRADO")


def procurar_produto():
    produto = input("Localizar: ").title()
    if produto in estoque:
        indice = estoque.index(produto)
        print(f"{produto} foi encontrado no indice {indice}")
    else:
        print(f"{produto} não foi encontrado")


def listar_produtos():
    if not estoque:
        print("Estoque vazio!")
    else:
        print("=" * 37)

        for i, p in enumerate(estoque, start=1):
            print(f"{i}. {p}")

    print("=" * 37)
    print("[V] Voltar | [C] Cadastrar | [R] Remover")


def quantidade_produto():
    print(f"Total de produtos cadastrados: {len(estoque)}")


def limpar_estoque():
    concluir = input("Tem certeza? [S/N]").upper()

    if concluir == "S":
        for i in range(101):
            print(f"\rApagando {i} % ", end="", flush=True)
            tempo(0.03)

        limpar_tela()
        print("Estoque apagado com sucesso")
        estoque.clear()


while True:

    limpar_tela()
    menu()

    try:
        op = int(input(""))
        limpar_tela()

        match op:
            case 1:
                cadastrar_produto()
                tempo(1)
            case 2:
                remover_produto()
                tempo(1)
            case 3:
                alterar_produto()
                pausa()

            case 4:
                procurar_produto()
                pausa()

            case 5:
                while True:
                    limpar_tela()
                    listar_produtos()
                    sair = input(": ").upper()
                    print("=" * 37)

                    if sair == "V":
                        break
                    elif sair == "C":
                        cadastrar_produto()
                        pausa()
                        break
                    elif sair == "R":
                        remover_produto()
                        pausa()
                        break
                    else:
                        print("!ERRO: OPÇÃO INVALIDA")
                        pausa()

            case 6:
                quantidade_produto()
                pausa()

            case 7:
                limpar_estoque()
                pausa()

            case 0:
                print("Encerrando...")
                tempo(0.5)
                break
            case _:
                print("!ERRO: OPÇÃO INVALIDA")
                pausa()
    except ValueError:
        print("!ERRO: DIGITE APENAS NUMEROS")
        pausa()
