m = "".center(30, "=")

print(m)
print("Escola de Doido".center(30))
print(m)

c = 1
q_a = int(input("Quantos alunos tem na sala? "))
m_nota = 0
m_aluno = str
print(m)

while c <= q_a:
    print(f"Aluno {c}")
    nome = input("Nome do aluno: ").title()
    nota = float(input(f"Nota de {nome}: "))
    print(m)
    c += 1

    if nota > m_nota:
        m_nota = nota
        m_aluno = nome


print(f"O melhor aproveitamento foi de {m_aluno} com nota {m_nota}")
