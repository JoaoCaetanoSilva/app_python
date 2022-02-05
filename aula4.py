nota = int(input('Entre com a nota: '))
while nota > 10:
    nota = int(input('(Nota invalida!) \nNota correta: '))

a = nota
while a < 10:
    print(a)
    a += 1

# a = int(input('Entre com um valor: '))
#
# div = 0
# for x in range(1, a+1):
#         resto = a % x
#         if resto == 0:
#             div = div + 1
#
# if div == 2:
#         print('Numero {} é primo'.format(a))
# else:
#     print('Numero {} não é primo'.format(a))

