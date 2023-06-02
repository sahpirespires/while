pares = 0
while True:
    inicio = int(input("digite um némero [digite 0 para parar]:"))
    if inicio % 2 == 0:
        pares += inicio
    if inicio == 0:
        print(f"Soma dos números pares: {pares}")
        break