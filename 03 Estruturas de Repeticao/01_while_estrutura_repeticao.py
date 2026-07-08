import time

nros = 0

while nros <= 100:
    print(f"\rCarregando... {nros} % ", end=" ", flush=True)
    time.sleep(0.1)
    nros = nros + 1

print()
mensagens = "Arquivo enviado com sucesso !"

for msg in mensagens:
    print(msg, end="", flush=True)
    time.sleep(0.1)

print()
