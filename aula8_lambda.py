digite = input('Palavra: ')
lista_animais = []
lista_animais = digite.split()

contador_letras = lambda lista: [len(x) for x in lista]
print('Total de letras: {}'.format(contador_letras(lista_animais)))

print('/')

soma = lambda a, b: a + b
print('A soma dá: {}'.format(soma(2, 3)))

print('/')

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'divisao': lambda a, b: a / b,
    'multiplicacao': lambda a, b: a * b,
}

print(type(calculadora))

print('/')

soma = calculadora['soma']
subtracao = calculadora['subtracao']
divisao = calculadora['divisao']
multiplicacao = calculadora['multiplicacao']

print('O total da soma dá: {}'.format(soma(2, 3)))
print('O total da subtracao dá: {}'.format(subtracao(3, 3)))
print('O total da divisao dá: {}'.format(divisao(4, 8)))
print('O total da multiplicacao dá: {}'.format(multiplicacao(7, 4)))