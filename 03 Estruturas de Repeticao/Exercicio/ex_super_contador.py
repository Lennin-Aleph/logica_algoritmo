import time

m = "".center(17, "=")
c = 0
opcao = 0

while opcao != 3:
    print(m)
    print("|", "Menu".center(13), "|")
    print(m)
    print("| [1] De 1 a 10 |")
    print("| [2] De 10 a 1 |")
    print("| [3] Sair      |")
    print(m)
    opcao = int(input(""))

    match opcao:
        case 1:
            c = 1
            while c <= 10:
                print(f"\rContando: {c} ", end=" ", flush=True)
                time.sleep(0.5)
                c += 1
            print()
        case 2:
            c = 10
            while c >= 1:
                print(f"\rContando: {c} ", end=" ", flush=True)
                time.sleep(0.5)
                c -= 1
            print()
        case 3:
            msg = "Saindo..."
            for i in msg:
                print(i, end="", flush=True)
                time.sleep(0.1)
            print()
print(m)
