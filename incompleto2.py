texto = (input('Texto: '))
encontrar = (input('Palavra: '))
lista = texto.split()

if encontrar in lista:
    print('Esta na lista!')

    import re
    a = encontrar
# Obs: Deveria ser "lista" no lugar de texto. Para a contagem correta da posicao. Tipo: 0, 1 , 2.
    b = texto
    result = [_.start() for _ in re.finditer(a, b)]
    print('Na posição: ' + str(lista.index(encontrar)))

    print('Numero de ocorrencias no texto:')
    y = texto.count(encontrar)
    print(y)

# Obs: Printar texto mas com o valor pedido (encontrar) em vermelho. Tipo:(EM DESTAQUE).
    RED = "\033[1;31m"
    z = (RED + encontrar)
    print(texto + z)

else:
    RED = "\033[1;31m"
    print(RED + '\033[1mNão está na lista!\033[0m')

