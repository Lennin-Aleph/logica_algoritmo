# Contagem inteligente
import time

m = "".center(30, "=")

print(m)
print("Contador Inteligente".center(30))
print(m)

i = int(input("Inicio: "))
f = int(input("final: "))
print(m)

if i < f:
    while i <= f:
        print(f"Contando: {i}", flush=True)
        i += 1
        time.sleep(0.2)
else:
    while i >= f:
        print(f"Contando: {i}", flush=True)
        i -= 1
        time.sleep(0.2)
print(m)
