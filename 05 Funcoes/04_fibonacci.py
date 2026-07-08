import os, time

a = 0
b = 1


def topo():
    os.system("clear")
    m = "".center(100, "=")
    print(m)
    print("SEQUENCIA DE FIBONACCI".center(100))
    print(m)


def fibonacci(x, y, z):
    print(x, y, end=" ", flush=True)
    time.sleep(0.2)

    for i in range(3, z):
        f = x + y
        x = y
        y = f
        print(f, end=" ", flush=True)
        time.sleep(0.2)


topo()
c = int(input("Até qual sequencia? "))
fibonacci(a, b, c)
print()
