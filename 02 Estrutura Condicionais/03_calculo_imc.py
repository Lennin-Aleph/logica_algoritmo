massa = float(input("Massa (Kg) "))
altura = float(input("Altura (m) "))
IMC = massa / (altura * altura)

if IMC < 17:
    print(f"\nIMC : {IMC:.2f} \nMuito abaixo do peso\n")
elif IMC >= 17 and IMC < 18.50:
    print(f"\nIMC : {IMC:.2f} \nAbaixo do peso\n")
elif IMC >= 18.50 and IMC <= 25:
    print(f"\nIMC : {IMC:.2f} \nParabens! Peso ideal\n")
elif IMC > 25 and IMC < 30:
    print(f"\nIMC : {IMC:.2f} \nSobrepeso\n")
elif IMC >= 30 and IMC < 35:
     print(f"\nIMC : {IMC:.2f} \nObesidade\n")    
elif IMC >= 35 and IMC < 40:
     print(f"\nIMC : {IMC:.2f} \nObesidade Severa\n")
else:
    print(f"\nIMC : {IMC:.2f} \nObesidade Mórbida\n")
