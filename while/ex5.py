while True:
    inicio = str (input('digite o genero (m/f):'))
    if inicio != 'm' and inicio != 'f':
        print('errado')
        inicio = str(input('digite o gereno (m/f):'))
    else:
        break