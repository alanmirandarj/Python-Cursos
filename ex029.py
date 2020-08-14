velocidade = float(input('Qual a velocidade do carro ? : '))
if velocidade > 80:
    print('MULTADO, você esta acima da velocidade')
    print('-=-' * 20)
    multa = (velocidade-80) *7
    print('você deve pagar R$ {:.2f} ,'.format(multa))
print ('-=-' *20)
print('Tenha um bom dia, dirija com segurança')

