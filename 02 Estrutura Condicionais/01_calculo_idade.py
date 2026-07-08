# CONDICIONAL SIMPLES
MAIOR_IDADE = 18
ano_atual  = 2026
ano_nascimento = int(input("Qual ano voce nasceu? \n"))
idade_user = ano_atual - ano_nascimento

if idade_user >= MAIOR_IDADE:
    print("Maior de idade! \n Voce tem ", idade_user, "anos.")


