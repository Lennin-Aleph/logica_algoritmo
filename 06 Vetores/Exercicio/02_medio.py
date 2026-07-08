# Nível Médio
# Leia 10 números, armazene-os em uma lista e mostre:
# o maior número;
# o menor número;
# a soma de todos os números;
# a média.

numeros = []

for i in range(10):
    i *= 2
    numeros.append(i)

print(numeros)
print(f"Maior numero: {max(numeros)}")
print(f"Menor numero: {min(numeros)}")
print(f"Soma dos numero: {sum(numeros)}")
print(f"Media dos numero: {sum(numeros) / len(numeros)}")
