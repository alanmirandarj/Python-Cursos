#Escreva um programa pra aprovar um emprestimo pra comprar a casa , o programa vqai perguntar valor da casa,
# quantos anos ele vai pagar
#salario,
#calcule o valor da prestação sabendo que ele nãpo pode exeder o valor de 30 % do salario se nao sera negado
valor = float(input('Digite o valor da casa que quer comprar :'))
anos = int(input('Digite em quantos anos você quer pagar : '))
salario = float(input('Digite o valor de sua renda bruta :'))
ano = anos * 12
salarios = (salario * 30)/100
parcela = valor/ano

if salarios < valor / ano:
        print('Sua renda não comporta um financimaneto de R$ {}'.format(valor))
else:
        print(' o valor da sua parcela sera  de R${:.2f} dividida em {} meses '.format(parcela, ano))
print('-=-'*20)
