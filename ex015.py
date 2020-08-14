dias = int(input('Quantos dias alugado ? '))
km = float(input('Quantos Km rodados ? '))
pagar = (km*0.15)+(dias*60)
print('O cliente deve pagar R${:.2f} pelos {:.0f} dias de uso e {:.0f} KM percorridos'.format(pagar, km, dias))
