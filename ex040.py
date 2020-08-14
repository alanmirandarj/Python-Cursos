#calcule a media de duas notas com mensagme de aprovado:acima de 7 recuperação ate 6.9 e reprov abaixo de 5
n1= float(input('Digite a sua primeira nota :'))
n2 = float(input('Digite sua segunda nota :'))
resultado = (n1 + n2)/2
if resultado >= 7:
    print('Parabéns vocÊ foi aprovado com a nota {} e {} a media de {} acima de 7.0 !!'.format(n1, n2, resultado))
elif resultado < 5:
    print('Com {} e {} media foi de {} , esta abaixo de 5.0 e você esta reprovado !!'.format(n1, n2, resultado))
elif resultado >= 5:
    print('Com {} e {} a media foi de {}  e voce esta de recuperação!!'.format(n1, n2, resultado))
else:
    print('A nota informada esta incorreta , digite novamente')
