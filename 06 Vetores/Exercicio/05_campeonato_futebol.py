import os

times = []


for i in range(1, 4):
    time = input(f"Nome do {i}° time: ")
    times.append(time)

os.system("cls" if os.name == "nt" else "clear")
print("TABELA PARTIDAS".center(30))
print("=" * 30)

for i in range(len(times)):
    for j in range(len(times)):
        if i != j:
            print(f"{times[i]:<12} [] x []   {times[j]}")
