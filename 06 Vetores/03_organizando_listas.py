vetor = [1, 7, 5, 2, 6, 0]
ax = 0

print(vetor)
for i in range(len(vetor)):
    # i vale 0
    for j in range(i + 1, len(vetor)):
        # j vale 1 / j recebe o valor de i atual + 1
        if vetor[i] > vetor[j]:
            # i = 0 / j = 1
            aux = vetor[j]

            vetor[j] = vetor[i]
            vetor[i] = aux
print(vetor)
