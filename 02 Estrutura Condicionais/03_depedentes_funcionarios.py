nome_funcionario = input("Nome do funcionario: ")
salario = float(input("Salario do funcionario: R$ "))
nro_depedente = int(input("Quantidade de dependentes: "))
n_salario = float

match nro_depedente:
    case 0:
        n_salario = salario + (salario * 0.05)
    case 1:
        n_salario = salario + (salario * 0.10)
    case 2:
        n_salario = salario + (salario * 0.15)
    case 3:
        n_salario = salario + (salario * 0.20)
    case _:
        n_salario = salario + (salario * 0.25)

print(f"\nFuncionario(a) {nome_funcionario.title()} tem {nro_depedente} dependentes.")
print(f"Salario atual é R$ {salario}\nNovo salario sera de R$ {n_salario}")