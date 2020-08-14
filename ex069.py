
m = 0
f = 0
maior = 0
while True:
    print('-------Cadastre uma pessoa-------')
    print('---'*20)
    p=int(input('Idade :'))
    if p > 18:
        maior+=1
    print('---'*20)
    sexo= str(input('Sexo [F]/[M] :')).strip().upper()[0]
    while sexo not in 'MmFf':
        sexo = str(input('digite [F] para Feminino e [M] para Masculino :'))
        if sexo =='M':
            m+=1
        elif sexo == 'F':
            if p < 20:
             f+=1
    q= str(input('Quer continuar ? [S]/[N]')).strip().upper()[0]
    if q =='N':
        break

print(f'Total de pessoas com mais de 18 anos : {maior} ')
print(f'Ao todo temos {m} homem cadastrado')
print(f'E temos {f} mulheres com menos de 20 anos')