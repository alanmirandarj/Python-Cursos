num = []
maior = 0
menor = 0
for s in range (0,5):
    num.append(int(input(f'Digite um numero na posição {s}: ')))
    if s == 0:
        maior=menor=num[s]
    else:
         if num[s] > maior:
           maior = num[s]
         if num[s] < menor:
           menor = num[s]
print('===*==='*10)
print(f'Você digitou os valores {num}')
print(f'O maior valor digitado {maior} nas posições ....',end='')
for i , v in enumerate(num):
  if v==maior:
    print(f'{i+1}...',end='')
print(f' o menor valor digitado foi {menor} nas posições {s}... ',end='')
for i , v in enumerate(num):
  if v==menor:
    print(f'{i+1}...',end='')
