'''crie um tupla com os 20 primeiro colocados no brasileirao
os cinco primeiros são
os quatro ultimo sao
time em ordem alfabeticas
o chapeconhe esta na ? posicao'''
lista = ('Flamengo','Santos','Palmeiras','Grêmio','Athletico Paranaense','São Paulo','Internacional',\
        'Corinthians','Fortaleza','Goiás','Bahia','Vasco da Gama','Atlético','Fluminense','Botafogo',\
        'Ceará','Csa','Chapecoense','Avaí')
print('======'*30)
print(f'Lista de times do campeonato brasileiro : {lista}')
print('======'*30)

print(f'Os 5 primeiros são :{lista[:5]}')
print('======'*30)
print(f'Os 4 ultimos são :{lista[-4:]}')
print('======'*30)
print(f'Times em ordem alfabetica: {sorted(lista)}')
print(f'O {lista[17]} esta na {lista.index("Chapecoense")}ª posição ')
