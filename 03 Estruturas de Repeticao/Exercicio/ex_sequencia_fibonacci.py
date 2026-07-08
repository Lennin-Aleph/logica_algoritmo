import time

a = 0
b = 1
c = 0

m = "".center(30, "=")
print(m)
print("Sequencia de Fibonacci".center(30))
print(m)

print(a, b, end=" ", flush=True)
time.sleep(0.5)


for i in range(15):
    c = a + b
    a = b
    b = c

    print(c, end=" ", flush=True)
    time.sleep(0.5)

print()
