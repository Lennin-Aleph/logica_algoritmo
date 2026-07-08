import time, os

x = 0
y = 1


def topo():
    os.system("clear")
    m = "".center(100, "=")
    print(m)
    print("SEQUENCIA DE FIBONACCI".center(100))
    print(m)


def fibonacci(a, b, c):
    print(a, b, end=" ", flush=True)
    time.sleep(0.3)

    for i in range(3, c):
        d = a + b
        a = b
        b = d
        print(d, end=" ", flush=True)
        time.sleep(0.3)


topo()
z = int(input("Quantos numeros da sequencia? "))
topo()

fibonacci(x, y, z)
print()
