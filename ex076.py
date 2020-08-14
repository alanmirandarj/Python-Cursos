'''crie um programa que tenha uma tupla unica com nomes de produto e respectivos preços na seguencia
no final mostre os preços organizando os dados em forma tabular'''
'''listagem de preço '''

lista = ('Lapis',1.75,
         'Borracha', 0.50,
         'Caderno', 5.0,
         'Estojo', 4.0,
         'Caneta',3.0,
         'Mochila',35.0,
        'Borracha', 0.50,
         'Caderno', 5.0,
         'Estojo', 4.0,
         'Caneta',3.0,
         'Mochila',35.0,
         'Livro',25.0)
print('===='*30)
print(f'{"LISTAGEM DE PREÇOS":^80}')
print('===='*30)
for pos in range(len(lista)):
    if pos % 2 == 0:
      print(f'{lista[pos]:.<30}',end='')
    else:
      print(f'R${lista[pos]:>7.2f}')
print('===='*30)
