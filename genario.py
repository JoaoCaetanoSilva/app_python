textoCapturado1 = input('Primeiro bimestre: ')

lista = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

contemAlfa = False

for caracterLido in textoCapturado1:
    if caracterLido not in lista:
        contemAlfa = True

if(not contemAlfa):
    numeroCapturado1 = int(textoCapturado1)
    print('O valor digitado e um numero')




# media = (numeroCapturado1 + numeroCapturado2 + numeroCapturado3 + numeroCapturado4) / 4
# if numeroCapturado1 <= 10 and numeroCapturado2 <= 10 and numeroCapturado3 <= 10 and numeroCapturado4 <= 10:
#     print('Media: {}'.format(media))


numeroCapturado1 = int(textoCapturado1)