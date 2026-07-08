import time

nros = 10

while nros >= 0:
    print(f"\rContagem Regressiva {nros} ", end=" ", flush=True)
    time.sleep(1)
    nros = nros - 1

print()
print("Tempo esgotado !")
