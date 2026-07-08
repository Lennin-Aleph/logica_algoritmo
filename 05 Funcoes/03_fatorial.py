n = int(input("Digite um numero: "))


def fatorial(v):
    resultado = 1
    numero = v

    for i in range(numero, resultado, -1):
        resultado *= i

    return resultado


f = fatorial(n)
print(f"{n}! = {f}")
