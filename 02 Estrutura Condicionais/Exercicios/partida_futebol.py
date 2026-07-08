#CABEÇALHO
menu = "".center(30, "=")
print(menu)
print("SÃO PAULO X SANTOS".center(30))
print(menu)

#ENTRADA USUARIO
gols_tricolor = int(input("Quantos gols do São Paulo? "))
gols_santos = int(input("Quantos gols do Santos? "))
print(menu)

#CALCULANDO GOLS
diferenca_gols = abs(gols_santos - gols_tricolor)
partida = ""

#RESULTADO PARTIDA
match diferenca_gols:
    case 0:
        partida = "EMPATE"
    case 1 | 2 | 3:
        partida = "PARTIDA NORMAL"
    case _:
        partida = "GOLEADA"

print(f"DIFERENÇA DE GOLS: {diferenca_gols}".center(30))
print(f"STATUS: {partida}".center((30)))
print(menu)
