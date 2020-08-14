#calcule o valor do produto
# considerando a forma de pagamento a vista em dinheiro ou cheque c/10% de desconto,
# a vista no cartão 5% de desconto, 2x no cartao preço normal mais de 2x com 20 % de juros
produto = float(input('Digite o valor do produto :'))
print('''Qual a forma de pagamento ?
[1] A vista em dinheiro ou cheque
[2] A vista no cartão
[3] 2 x no cartão 
[4] Mais de 2 x no cartão ''')
pag = float(input('Escolha uma opção de pagamento'))
print('-=-'*20)
if pag == 1:
    total = produto - (produto * 10 /100)
    print('O valor do produto a pagar é R$ {:.3f} '.format(total))
elif pag == 2:
    total = produto - (produto * 5 / 100)
    print('O valor do produto a pagar é R$ {:.3f} '.format(total))
elif pag == 3:
    total = produto
    print('O valor do produto a pagar é R$ {:.3f} '.format(total))
elif pag == 4:
    total = (produto*20/100)+produto
    print('O valor do produto a pagar é R$ {:.3f} '.format(total))
else:
    print('escolha um numero de 1 a 4')


