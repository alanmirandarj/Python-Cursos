#calcule o imc e mostre seu status abaixo de 18.5:Abaixo do peso, entre 18.5 e 25 peso ideal,25 a 30 sobrepeso,
# 30 a 40 obsidade e de 40 acima absidade morbida
peso = float(input('Qual seu peso ?'))
altura = float(input('Qual sua altura ?'))
imc = peso / (altura * altura)
print(' O IMC dessa pessoa é {:.1f} ,'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 24.9:
    print('Peso normal')
elif imc < 29.9:
    print('Sobrepeso')
elif imc < 34.9:
    print('Obsidade grau 1')
elif imc < 39.9:
    print('Obsidade grau 2')
elif imc > 40:
    print('Obsidade grau 3 ')







