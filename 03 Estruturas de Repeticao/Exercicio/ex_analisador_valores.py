m = "".center(25, "=")
soma = 0
div5 = 0
vlr_nulo = 0
nro_par = 0
soma_par = 0

print(m)
print("Analisador de Valores".center(25))
print(m)

for i in range(1, 6):
    valor = int(input(f"Digite o {i}° valor: "))
    soma += valor

    if valor % 5 == 0:
        div5 += 1

    if valor == 0:
        vlr_nulo += 1

    if valor % 2 == 0:
        nro_par += 1
        soma_par += valor


media = soma / 5

print(m)
print(f"A soma dos valores é de {soma}")
print(f"A media dos valores é de {media}")
print(f"Valores divisiveis por cinco: {div5}")
print(f"Valores nulos: {vlr_nulo}")
print(f"Soma dos numeros pares: {soma_par}")
