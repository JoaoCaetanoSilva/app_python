# nome = input('Qual seu nome?')
# print('Prazer conhece-lo, {}'.format(nome))
# # or
# print('Prazer conhece-lo,', nome)
# # or
# print('Prazer conhece-lo, ' + nome)
# ()()()()()()()()()()()()()()()()()()()()()()()()
# n1 = int(input('valor 1: '))
# n2 = int(input('valor 2: '))
# z = n1 + n2
# print('A soma entre {}'.format(n1), 'e {}'.format(n2), 'é de: {}'.format(z))
# # or
# print('A soma entre {} e {} é de: {}'.format(n1, n2, z))
# # or
# print('A soma entre', n1, 'e', n2, 'é de:', z)
digite = input('Digite qualquer coisa: ')
print('Qual o tipo??\nR:', type(digite))
print('Está em branco??\nR:', digite.isspace())
print('São numeros?\nR:', digite.isnumeric())
print('São apenas letras?\nR:', digite.isalpha())
print('São apenas numeros?\nR:', digite.isalnum())
print('Está apenas em maiusculo?\nR:', digite.isupper())
print('Esta apenas em minusculo?\nR:', digite.islower())
print('Esta mesclada?\nR:', digite.istitle())