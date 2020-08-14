av1 = int(input('Advinhe o numéro de 0 a 5 que estou pensando : '))
av2 = float(input('Digite sua nota Av2 : '))
media = (av1 + av2) / 2
if media >= 6.0:
    print('Parabéns sua nota foi {} você foi aprovado !'.format(media))
else:
    print('Infelizmente você não passou, sua nota de {} não foi o suficiente, '.format(media))
