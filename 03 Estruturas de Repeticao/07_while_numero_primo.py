n = int(input("Digite um numero: "))
c = 0
num_div = 0

while n >= c:
    c += 1

    if (n % c) == 0:
        num_div += 1


if num_div > 2:
    print(f"O numero {n} não é primo!")
else:
    print(f"O numero {n} é primo")
