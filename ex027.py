nome = str(input('Digite seu nome completo : ')).strip()
n = nome.split()
print("Muito prazer em te conhecer {} \nSeu primeiro nome é: {} \nSeu ultimo nome é: {}".format(nome, n[0], n[-1] ))
