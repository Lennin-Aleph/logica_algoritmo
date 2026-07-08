mat_ID = []

for i in range(4):
    mat_ID.append([i, i, i, i])

for l in range(4):
    for c in range(4):
        if l == c:
            mat_ID[l][c] = 1
        else:
            mat_ID[l][c] = 0

for l in range(4):
    for c in range(4):
        print(mat_ID[l][c], end="  ", flush=True)
    print()
