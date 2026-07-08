import os

alunos = []
nota1 = []
nota2 = []
media = []


def limpa_tela():
    os.system("cls" if os.name == "nt" else "clear")


for i in range(3):
    a = input("Nome do aluno: ").title()
    alunos.append(a)

    n1 = float(input("Nota 1: "))
    nota1.append(n1)

    n2 = float(input("Nota 2: "))
    nota2.append(n2)

    m = (nota1[i] + nota2[i]) / 2
    media.append(m)

    limpa_tela()

print("LISTAGEM ALUNOS")
print("=" * 10)

for i in range(3):
    print(f"{alunos[i]}\n{media[i]}")
