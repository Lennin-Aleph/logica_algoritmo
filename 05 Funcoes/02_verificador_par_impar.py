import os, time

v = int
sair_sistema = "Encerrando... "

while v != 0:
    v = int(input("Digite um numero: "))

    def topo():
        os.system("clear")
        t = "".center(50, "=")
        t2 = "".center(50, "-")
        print(t)
        print("|", "VERIFICADOR DE PAR OU IMPAR".center(46), "|")
        print(t)
        print("|", "Para encerrar digite [0]".center(46), "|")
        print(t2)

    def par_impar(n):
        if n % 2 == 0:
            return f"O numero {n} é [PAR]"
        else:
            return f"O numero {n} é [IMPAR]"

    topo()
    r = par_impar(v)
    print(r)


for i in sair_sistema:
    print(i, end="", flush=True)
    time.sleep(0.2)
