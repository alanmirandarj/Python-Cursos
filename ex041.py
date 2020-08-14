# saber a categoria pelo ano idade 9 anos - mirim ,
# ate 14 anos infantil/ate 19 junior até 20 senior/acima de 20 master
from datetime import date
idade = int(input('Digite o ano de nascimento : '))
atual= date.today().year
cat = atual - idade
if cat <= 9:
    print('Sua categoria é mirim ')
elif cat <= 14:
    print('voce nasceu {} sua categoria é infantil'.format(idade))
elif cat <= 19:
    print('Sua categoria é junior')
elif cat >20:
    print('Sua categoria e master!')
else:
    print('sua categoriaé senior')
