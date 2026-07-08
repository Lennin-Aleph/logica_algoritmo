import os

gabarito = []
alunos = []
resp_alu = []
nota = []


def lp():
    os.system("cls" if os.name == "nt" else "clear")


print("PASSO 1 - Cadastro de Gabarito".center(25))
print("-" * 25)

for i in range(1, 6):
    r = input(f"Questão {i}: ")
    gabarito.append(r)


for i in range(1, 4):
    p = 0
    n = 0
    lp()
    print("-----------------------")
    print(f"ALUNO {i}")
    print("-----------------------")

    nome = input("Nome: ").title()
    alunos.append(nome)
    print("RESPOSTAS DADAS\n")

    for i in range(len(gabarito)):
        p += 1
        r = input(f"Questão {p}: ")

        if r == gabarito[i]:
            n += 2

    nota.append(n)

lp()
print("NOTAS FINAIS".center(25))
print("-" * 25)

for i in range(len(alunos)):
    print(f"{alunos[i]:<15} {nota[i]:.1f}")

mt = sum(nota) / len(alunos)
print("-" * 25)
print(f"Media da turma:  {mt:.1f}")
