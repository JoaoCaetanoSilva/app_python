a = int(input('Primeiro bimestre: '))
while a > 10:
    a = int(input('(VOCE DIGITOU ERRADO). \nPrimeiro bimestre: '))
b = int(input('Segundo bimestre: '))
while b > 10:
    b = int(input('(VOCE DIGITOU ERRADO). \nSegundo bimestre: '))
c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input('(VOCE DIGITOU ERRADO). \nTerceiro bimestre: '))
d = int(input('Quarto bimestre: '))
while d > 10:
    d = int(input('(VOCE DIGITOU ERRADO). \nQuarto bimestre: '))
media = (a + b + c +d) / 4
if a <= 10 and b <= 10 and c <= 10 and d <= 10:
     print('Media: {}'.format(media))

# a = int(input('Entre com o primerio valor: '))
# b = int(input('Entre com o primerio valor: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or resto_b == 0:
#     print('Foi digitado um numero par')
# else:
#     print('Nenhum numero par foi digitado')

# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
#
# if a > b and a > c:
#     print('O maior numero é: {}'.format(a))
# if b > a and b > c:
#     print('O maior numero é: {}'.format(b))
# else:
#     print('O maior numero é: {}'.format(c))
# print('Final do programa')
