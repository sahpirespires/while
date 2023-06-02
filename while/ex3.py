res = "s"
while res == "s":
    numero = int (input('digite aqui:'))
    if numero == 999 or numero < 0:
        print('número grande')
        break
        res= str(input('quer continuar? (sim/não):'))