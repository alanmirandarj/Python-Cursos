'''crie um programa com varias palavras e deve mostrar as vogais de cada palavra'''
palavra = 'imoveis', 'apartamento', 'casa', 'carro', 'liberdade', 'corretor', \
          'terreno', 'imobiliaria', 'cury', 'proposta', 'venda'
for p in palavra:
    print(f'\nNa palavra {p} temos :', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')
f