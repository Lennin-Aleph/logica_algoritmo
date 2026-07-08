import os

mat_id = []
soma_dp = 0
vlr_mul = 1
m_v = 0


def lp():
    os.system("cls" if os.name == "nt" else "clear")


for i in range(4):
    mat_id.append([i, i, i, i])

for i in range(4):
    for j in range(4):
        lp()
        r = int(input(f"Valor da posição [{i}][{j}]:  "))
        mat_id[i][j] = r

        if i == j:
            soma_dp += r

for i in mat_id[1]:
    vlr_mul *= i

for i in range(4):
    for j in range(4):
        if j == 2:
            r = mat_id[i][j]
            if r > m_v:
                m_v = r


lp()
largura = max(len(linha) for linha in mat_id) + 2

for i in mat_id:
    for j in i:
        print(f"{j:>{largura}}", end=" ")
    print()

print(f"\nA soma total da diagonal principal foi de {soma_dp}")
print(f"O valor total multiplicado da 2° linha foi de {vlr_mul}")
print(f"O maior valor da 3° linha foi de {m_v}")
