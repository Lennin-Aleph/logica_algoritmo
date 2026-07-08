import time

c = int(input("Contar até: "))
entrada_user = input("Forma de contagem:\n[N] Normal\n[P] Par\n[I] Impar\n").upper()
i = 0

if entrada_user == "P":
    print("Só numeros pares: ")

    while i <= c:
        print(i, end=" ", flush=True)
        i += 2
        time.sleep(0.3)

elif entrada_user == "I":
    print("Só numeros impar: ")
    i = 1

    while i <= c:
        print(i, end=" ", flush=True)
        i += 2
        time.sleep(0.3)

else:
    if entrada_user == "N":
        print("Contagem normal: ")
    else:
        print("Não foi feita a escolha, segue a contagem normal: ")
    while i <= c:
        print(i, end=" ", flush=True)
        i += 1
        time.sleep(0.3)

print("\nFim\n")
