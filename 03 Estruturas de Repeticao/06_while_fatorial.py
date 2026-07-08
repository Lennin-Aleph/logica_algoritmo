mn = "".center(30, "=")
o = ""

while o != "S":
    print(mn)
    print("Calculadora de Fatorial".center(30))
    print(mn)

    n = int(input("Fatorial de "))
    print(mn)
    c = n
    f = 1

    while c >= 1:
        f *= c
        c -= 1

    print(f"Fatorial de {n} é {f}")
    print(mn)
    o = input("Digite uma opção:\n[S] Sair / [C] Continuar\n").upper()
    print(mn)

    if o != "S" and o != "C":
        print("Opção invalida!")
        print(mn)

print("Encerrando...")
