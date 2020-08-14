nome = str(input('Digite uma frase :')).strip().upper()
palavras = nome.split()
juntos = ''.join(palavras)
#inverso = ''
inverso = juntos[::  -1]
'''for letra in range(len(juntos)-1,-1,-1):
    inverso += juntos[letra]'''
if inverso == juntos:
        print('Temos um palindromo')

print('Você digitol a frase {} e seu inverso é {} '.format(juntos, inverso))
