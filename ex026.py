frase = str(input('Digite uma frase : ')).upper().strip()#O STRIP TIRAR OS ESPAÇOS /UPPER COLOCA O TEXTO EM MAICULA
print('A letra a aparece {} '.format(frase.count('A')))#O COUNT FAZ A CONTAGEM DA LETRA
print('A primeira A aparece na posição {} '.format(frase.find('A')+1))#FIND FALA A POSICÇÃO DA PRIMEIRA LETRA A E O + 1 COLOCA A CONTAGEM UM ACIMA PQ A CONTAGEM COMEÇA EM ZERO
print('A ultima letra A aparece na posição {} '.format(frase.rfind('A')+1))#RFIND FALA A POSIÇÃO DA ULTIMA LETRA ESCOLHIDA E + 1 ORGANIZA A POSIÇÃO
