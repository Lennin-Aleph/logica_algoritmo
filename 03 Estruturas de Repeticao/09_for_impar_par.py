import time

m = "".center(30, "=")
print(m)
print("IMPAR OU PAR INTELIGENTE".center(30))
print(m)

vlr = int(input("Digite um numero: "))
print(m)
pergunta = input("[I] Icrementar\n[D] Decrementar ").upper()
print(m)
par_impar = input("[p] Par\n[i] Impar ").lower()
print(m)
v1 = int
v2 = int
v3 = int

if pergunta == "I":
    v3 = 2
    v2 = vlr

    if par_impar == "p":
        v1 = 0
    else:
        v2 += 1
        v1 = 1

else:
    v3 = -2
    v2 = 0

    if par_impar == "p":
        v1 = vlr
        if vlr % 2 == 1:
            vlr -= 1
            v1 = vlr
    else:
        v1 = vlr
        if vlr % 2 == 0:
            vlr -= 1
            v1 = vlr


for i in range(v1, v2, v3):
    print(i, end=" ", flush=True)
    time.sleep(0.1)

print()
print(m)
