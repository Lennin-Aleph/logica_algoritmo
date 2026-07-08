# CONDICIONAL ANINHADO
massa = float(input("\nMassa (Kg) "))
altura = float(input("Altura (m) "))
IMC = massa / (altura * altura)

if IMC < 18.50:
    if IMC >= 17:
        print(f"\nIMC : {IMC:.2f} \nAbaixo do peso\n")
    else:
        print(f"\nIMC : {IMC:.2f} \nMuito abaixo do peso\n")
else:
    if IMC <= 25:
        print(f"\nIMC : {IMC:.2f} \nParabens! Peso ideal\n")
    elif IMC < 30:
        print(f"\nIMC : {IMC:.2f} \nSobrepeso\n") 
    else:
        if IMC < 35:
            print(f"\nIMC : {IMC:.2f} \nObesidade\n")
        elif  IMC < 40:
            print(f"\nIMC : {IMC:.2f} \nObesidade Severa\n")
        else:
            print(f"\nIMC : {IMC:.2f} \nObesidade Mórbida\n")    
    