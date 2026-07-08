import os, time

jv = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
cx = 0


def lp():
    os.system("cls" if os.name == "nt" else "clear")


def menu():
    print(f"""
    +-----+-----+-----+
    |  {jv[0][0]}  |  {jv[0][1]}  |  {jv[0][2]}  |
    +-----+-----+-----+
    |  {jv[1][0]}  |  {jv[1][1]}  |  {jv[1][2]}  |
    +-----+-----+-----+
    |  {jv[2][0]}  |  {jv[2][1]}  |  {jv[2][2]}  |
    +-----+-----+-----+
    """)


while True:

    try:
        while True:
            lp()
            menu()

            jx = int(input("Jogar [X] em qual posição: "))
            encontrou = False

            for i in range(3):
                for j in range(3):

                    if jv[i][j] == jx:
                        jv[i][j] = "X"
                        encontrou = True
                        break

                if encontrou:
                    break

            if not encontrou:
                print("Posição invalida ou já jogada")
                time.sleep(1)

            else:
                break

        cx += 1
        lp()
        menu()

        if cx == 5:
            print("# DEU VELHA #")
            break
        # RESULTADO [X]
        elif jv[0][0] == "X" and jv[0][1] == "X" and jv[0][2] == "X":
            print("[X] Ganhou !!")
            break

        elif jv[1][0] == "X" and jv[1][1] == "X" and jv[1][2] == "X":
            print("X Ganhou !!")
            break

        elif jv[2][0] == "X" and jv[2][1] == "X" and jv[2][2] == "X":
            print("[X] Ganhou !!")
            break

        elif jv[0][0] == "X" and jv[1][0] == "X" and jv[2][0] == "X":
            print("[X] Ganhou !!")
            break

        elif jv[0][1] == "X" and jv[1][1] == "X" and jv[2][1] == "X":
            print("[X] Ganhou !!")
            break

        elif jv[0][2] == "X" and jv[1][2] == "X" and jv[2][2] == "X":
            print("[X] Ganhou !!")
            break

        elif jv[0][0] == "X" and jv[1][1] == "X" and jv[2][2] == "X":
            print("[X] Ganhou !!")
            break

        elif jv[0][2] == "X" and jv[1][1] == "X" and jv[2][0] == "X":
            print("[X] Ganhou !!")
            break

        while True:
            lp()
            menu()
            jo = int(input("Jogar [O] em qual posição: "))
            encontrou = False

            for i in range(3):
                for j in range(3):

                    if jv[i][j] == jo:
                        jv[i][j] = "O"
                        encontrou = True
                        break

                if encontrou:
                    break

            if not encontrou:
                print("Posição invalida ou já jogada")
                time.sleep(1)
            else:
                break

        lp()
        menu()

        # RESULTADO [O]
        if jv[0][0] == "O" and jv[0][1] == "O" and jv[0][2] == "O":
            print("[O] Ganhou !!")
            break

        elif jv[1][0] == "O" and jv[1][1] == "O" and jv[1][2] == "O":
            print("[O] Ganhou !!")
            break

        elif jv[2][0] == "O" and jv[2][1] == "O" and jv[2][2] == "O":
            print("[O] Ganhou !!")
            break

        elif jv[0][0] == "O" and jv[1][0] == "O" and jv[2][0] == "O":
            print("[O] Ganhou !!")
            break

        elif jv[0][1] == "O" and jv[1][1] == "O" and jv[2][1] == "O":
            print("[O] Ganhou !!")
            break

        elif jv[0][2] == "O" and jv[1][2] == "O" and jv[2][2] == "O":
            print("[O] Ganhou !!")
            break

        elif jv[0][0] == "O" and jv[1][1] == "O" and jv[2][2] == "O":
            print("[O] Ganhou !!")
            break

        elif jv[0][2] == "O" and jv[1][1] == "O" and jv[2][0] == "O":
            print("[O] Ganhou !!")
            break

    except ValueError:
        print("ERRO!   DIGITE APENAS NUMEROS")
        time.sleep(1)
