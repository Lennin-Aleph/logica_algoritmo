import os

m = "".center(20, "=")
m2 = "".center(20, "-")
r = int
opcao = ""
h_apto = 0
m_apto = 0

while opcao != "N":
    os.system("clear")
    print(m)
    print("SELETOR DE PESSOAS".center(20))
    print(m)

    sexo = input("Qual o sexo? [M/F] ").upper()
    idade = int(input("Qual a idade? "))
    cabelo = "Qual a cor do cabelo?"

    print(m2)
    print("[1] Preto")
    print("[2] Castanho")
    print("[3] Loiro")
    print("[4] Ruivo")
    r = int(input(""))
    print(m2)

    if sexo == "M" and idade >= 18 and r == 2:
        h_apto += 1
    elif sexo == "F" and r == 3:
        if idade >= 25 and idade <= 30:
            m_apto += 1

    opcao = input("Quer continuar? [S/N] ").upper()

print(m2)
print(f"Total de homens com mais de 18 anos e cabelo castanho: [{h_apto}]")
print(f"Total de mulheres entre 25 a 30  anos e cabelo loiro: [{m_apto}]")
