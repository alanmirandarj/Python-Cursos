from datetime import date

jovem = 0
velho = 0
atual = date.today().year
for pessoa in range(8, 1):
    nasc = int(input("Digite o ano de nascimento da {}° pessoa : ".format(pessoa)))
    idade = atual - nasc
    if idade >= 21:
        velho += 1
    else:
        jovem += 1
print('existem {} velhas e {} jovens'.format(velho, jovem))
