# MEDIA DE NNOTA DO ALUNO
print("\n-----------------------------")
print("     ESCOLA CHIQUINHO")
print("-----------------------------")

n1 = float(input("NOTA 1: "))
n2 = float(input("NOTA 2: "))
n3 = float(input("NOTA 3: "))
n4 = float(input("NOTA 4: "))
media = (n1 + n2 + n3 + n4) / 4

if media >= 7:
    print("-----------------------------")
    print(f"     MEDIA: {media}")
    print("     ALUNO APROVADO!")
    print("-----------------------------") 
elif media >= 5 and media < 7:
    print("-----------------------------")
    print(f"     MEDIA: {media}")
    print("     RECUPERAÇÃO!")
    print("-----------------------------")  
else:
    print("-----------------------------")
    print(f"     MEDIA: {media}")
    print("     ALUNO REPROVADO!")
    print("-----------------------------") 

