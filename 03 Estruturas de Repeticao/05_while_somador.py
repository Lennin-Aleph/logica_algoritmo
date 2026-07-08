cont = 1
s = 0
maior_vlr = 0

while cont <= 5:
    nro_user = int(input(f"Digite o {cont}° numero: "))
    cont += 1
    s += nro_user

    if nro_user > maior_vlr:
        maior_vlr = nro_user

print(f"\nSoma total dos numeros: {s}")
print(f"Maior valor foi: {maior_vlr}")
