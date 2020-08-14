salario = float(input('Qual o valor so salario : '))
if salario <= 1250:
    novo=salario * 15 /100 + salario
else:
    novo=salario * 10 /100 + salario

print('Quem ganhava {:.2f} \nComeça a ganhar {:.2f} '.format(salario, novo))




