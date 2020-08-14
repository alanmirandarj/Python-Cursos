velho = 0
F = 0
media = 0
nomevelho = ''

for p in range(1,5):
    print('------{}ª PESSOA -----------'.format(p))
    nome = str(input('NOME:')).strip()
    idade = int(input('IDADE:'))
    sexo = str(input('SEXO [F]/[M]')).strip()
    media += idade
    mulher = +1
    med = media/4
    if p == 1 and sexo in 'Mn':
        velho = idade
        nomevelho = nome
        if sexo in 'Mn' and idade > velho:
            velho = idade
            nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        F += 1
print('O homen mais velho tem {} ano e se chama {} . '.format(idade,nomevelho))
print('A media de idade é de {} anos '.format(med))
print('Ao todos são {} mulheres com menos de 21 anos'.format(mulher))

