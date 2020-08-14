total = totmil = menor = conta = 0
barato = ' '
while True:
    produto = str(input('Nome do produto : '))
    valor = float(input('Preço do produto R$ : '))
    conta +=1
    total += valor
    if valor > 1000:
        totmil+=1
    if conta == 1 or valor < menor:
        menor = valor
        barato = produto
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar ? [S]/[N]')).strip().upper()[0]
    if cont == 'N':
        break
print('=======FIM DO PROGRAMA======')
print(f'O total das compras foram R$ {total}')
print(f'Temos {totmil} de produtos que custam mais de R$ 1.000,00 ')
print(f'O produto mais barato custa R$ {menor:.2f} e foi o {produto}')
