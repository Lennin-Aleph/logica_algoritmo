print("\n-----------------------------")
print("      CRIANÇA ESPERANÇA")
print("-----------------------------")
print("     Obrigado por ajudar! \n")
print(" [1] PARA DOAR R$ 10,00")
print(" [2] PARA DOAR R$ 20,00")
print(" [3] PARA DOAR R$ 35,00")
print(" [4] PARA DOAR R$ 45,00")
print(" [5] PARA DOAR OUTRO VALOR")
print(" [0] PARA CANCELAR")
opcao = int(input("\nESCOLHA UM OPÇÃO "))
valor = int

match opcao:
    case 0:
        valor = 0
    case 1:
        valor = 10
    case 2:
        valor = 20
    case 3:
        valor = 35
    case 4:
        valor = 45
    case 5:
        valor = float(input("Qual o valor da doação? R$ "))
    

print("\n-----------------------------")
print(f"    VALOR DOADO: R$ {valor:.2f}")
print("        OBRIGADO !")
print("-----------------------------\n")
