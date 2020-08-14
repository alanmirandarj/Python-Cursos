while True:
    print('~~~' * 30)
    numero = int(input('Digite o numero para ver sua tabuada :'))
    print('~~~' * 30)
    if numero < 0:
        break
    for c in range(1, 11):
        print('{} x {} = {} '.format(numero, c, numero * c))

print('FIM')
