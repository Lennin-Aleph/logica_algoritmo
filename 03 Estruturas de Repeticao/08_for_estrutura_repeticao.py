import time

for i in range(101):
    print(f"\rProgresso {i} % ", end=" ", flush=True)
    time.sleep(0.1)

for i in range(10, -1, -1):
    print(i, end=" ")

r = 0

for i in range(5):
    s = int(input("Digite um valor para somar: "))
    r += s

print(f"Resultado: {r}")
