from math import hypot
co = float(input('Qual o valor do comprimento do cateto oposto ? '))
ca = float(input('Qual o valor do cateto adjacente ? '))
hi = hypot(ca,co)
print('A hipotenusa vai medir {:.2f}'.format(hi))




"""co = float(input('Qual o valor do comprimento do cateto oposto ? '))
ca = float(input('Qual o valor do cateto adjacente ? '))
hi = (ca ** 2 + co ** 2) ** (1/2)
print('A hipotenusa vai medir {}'.format(hi))

p = float(input('Qual o comprimento do cateto oposto ? '))
a = float(input('Qual o comprimento do cateto adjacente ? '))
print('A hipotenusa vai medir {}'.format(float(((p**2+a**2)**(1/2))))
"""

