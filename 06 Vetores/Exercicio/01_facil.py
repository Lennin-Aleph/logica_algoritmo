# Nível Fácil
# Crie uma lista com 5 números informados pelo usuário e, ao final, exiba todos eles na ordem em que foram digitados.

lista = []

for i in range(1, 6):
    valor = int(input(f"Digite o {i}° numero: "))
    lista.append(valor)

print(lista)
