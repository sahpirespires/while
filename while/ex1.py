soma = 0
quantidade = 0
while True:
    inicio = float(input('Digite a nota:'))
    quantidade +=1
    soma += inicio
    if inicio < 0:
        media = soma / quantidade
        print(f"A media é de {media}")
        break
    final = str(input('Quer continuar?[sim/não]:'))
    if final == 'não':
        media = soma / quantidade
        print(f"A media é de {media}")
        break
