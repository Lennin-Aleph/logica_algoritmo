import os

cadeira = []


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def pausa():
    input("Pressione ENTER para continuar")


def cadastrar_cadeira():
    for i in range(1, 11):
        n = str(i)
        f = "B" + n
        cadeira.append(f)


def listar_cadeiras():
    for i in cadeira:
        print(f"[ {i} ]", end=" ", flush=True)

    print()
    print("-" * 70)


def reservar():
    try:
        acento = int(input("Reserva a cadeira: B"))

        if acento > 10 or acento <= 0:
            print("!ERRO!: OPÇÃO INVALIDA")

        else:
            acento = str(acento)
            acento = "B" + acento

            if acento in cadeira:
                i = cadeira.index(acento)
                cadeira[i] = "---"
                print(f"CADEIRA {acento} RESERVADA COM SUCESSO")
            else:
                print("!ERRO!: CADEIRA JÁ RESERVADA")

    except ValueError:
        print("! DIGITE APENAS NUMEROS !")


cadastrar_cadeira()

while True:
    limpar_tela()
    listar_cadeiras()
    reservar()

    try:
        pergunta = input("Quer reserva outra? [S/N]").upper()

        if pergunta == "S":
            pass

        elif pergunta == "N":
            limpar_tela()
            listar_cadeiras()
            print("SAINDO ...")
            break

        else:
            print("!ERRO!: OPÇÃO INVALIDA")
            pausa()
    except ValueError:
        print("!ERRO!")
        pausa()
