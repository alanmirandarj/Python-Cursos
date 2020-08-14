n = d = s = 0
n = int(input('Digite [999] para parar : '))
while n != 999:
    s += n
    d+=1
    n = int(input('Digite [999] para parar : '))


print('fim..você digitou {} numeros e o total é {}'.format(d , s))
