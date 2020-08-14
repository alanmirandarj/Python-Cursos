print('==='*30)
print('                                    BANCO ALAN         ')
print('==='*30)
saca = int(input('Qual valor você quer sacar R$ '))
total = saca
cin   = 50
totalced = 0
while True:
    if total >= cin:
        total -= cin
        totalced += 1
    else:
        if totalced > 0:
           print(f'Total de {totalced} cedulas de R$ {cin}')
        if cin == 50:
            cin = 20
        elif cin == 20:
            cin = 10
        elif cin == 10:
            cin = 1
        totalced = 0
        if total == 0:
            break




print('Volte sempre ao BANCO ALAN ! tenha um bom dia !')