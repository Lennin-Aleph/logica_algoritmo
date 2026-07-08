# ESTA APTO A DURIGIR?
print("\n-----------------------------")
print("  DEPARTAMENTO DE TRANSITO")
print("-----------------------------")

MAIOR_IDADE = 18
ano_atual = int(input("Ano Atual (yyyy): "))
ano_nasci = int(input("Ano de Nascimento (yyyy): "))
idade = ano_atual - ano_nasci

if idade >= MAIOR_IDADE:
    print("\n----------- STATUS -------------")
    print(f"    IDADE: {idade} ANOS ")
    print(f"    APTO A TIRAR A CARTEIRA")
    print("--------------------------------\n")
else:   
    print("\n----------- STATUS -------------")
    print(f"    IDADE: {idade} ANOS ")
    print(f"    NÃO PODE TIRAR A CARTEIRA")
    print("--------------------------------\n")
