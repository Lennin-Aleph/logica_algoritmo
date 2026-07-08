# Valores logicos
n1, n2, n3 = 2, 7, 5

print(n2 != n3)
print(n1 > n2)
print(n3 >= n1 + n2)
print(n2 / n1 >= n3)

a = int(input("Digite um numero: "))

if a % 2 == 0:
    print("Par")
else:
    print("Impar")


MAIOR_IDADE = 18
valor_pago = input("Pagou o boleto?  \nDigite s/n ")
idade_user = int(input("Qual sua idade? \n"))

if valor_pago == "s":
    valor_pago == True

    if idade_user >= MAIOR_IDADE and valor_pago:
        print("Pode tirar a habilitação")
    else:
        print("Menor de idade! \n Falta ", MAIOR_IDADE - idade_user, "anos para 18.")
else:
    print("Voce não fez o pagamento do boleto! ")


# Triangulo:
l1 = int(input("Qual o tamanho? "))
l2 = int(input("Qual o tamanho? "))
l3 = int(input("Qual o tamanho? "))

EQ = (l1 == l2) and (l2 == l3)
ES = (l1 != l2) and (l2 != l3) and (l1 != l3)
TRI = (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2)

print(f"Pode ser um triangulo? {TRI}")
print("o triangulo é equilatero? ", EQ)
print("o triangulo é escaleno? ", ES)
