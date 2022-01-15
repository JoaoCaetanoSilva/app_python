texto = (input('Texto: '))
encontrar = (input('Palavra: '))
lista = texto.split()

if encontrar in lista:
    print('\nEsta na lista!')

    ocorrencias = 0
    posicao = 0
    posicoes = ''
    for item in lista:
        if item == encontrar:
            ocorrencias += 1
            posicoes += str(posicao) + ', '
        posicao += 1

    print('Na posicao:' + posicoes[0:len(posicoes)-2])

    print('Numero de ocorrencias no texto:' + str(ocorrencias) + '\n\nTexto:')

    RED = "\033[1;31m"
    print(texto.replace( ' ' + encontrar, RED + ' ' + encontrar + '\033[0m'))

else:
    RED = "\033[1;31m"
    print(RED + '\033[1mNão está na lista!\033[0m')
