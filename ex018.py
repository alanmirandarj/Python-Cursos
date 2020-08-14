from math import radians, sin, cos, tan

v = int(input('Digite o angulo que deseja : '))
f = radians(v)
s = sin(f)
c = cos(f)
t = tan(f)
print('O angulo de {} tem o Seno {:.2f} '
      '\nO angulo de {} tem o Cosseno de {:.2f} '
      '\nO angulo de {} tem a tangente de {:.2f} '.format(v, s, v, c, v, t))

'''import math
v = int(input('Digite o  angulo que deseja :'))
s = math.sin(math.radians(v))
c = math.cos(math.radians(v))
t = math.tan(math.radians(v))

print('O angulo de {} tem o Seno {:.2f} '
      '\nO angulo de {} tem o Conseno de {:.2f} '
      '\nO angulo de {} tem a tangente de {:.2f} '.format(v,s,v,c,v,t) )
'''
