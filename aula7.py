texto = (input('Texto: '))
encontrar = (input('Palavra: '))
lista = texto.split()

if encontrar in lista:
    print(lista)
    print('Esta na lista!')

    import re
    a = encontrar
# Obs: Deveria ser "lista" no lugar de texto...
    b = texto
    result = [_.start() for _ in re.finditer(a, b)]
    print('Na posição: ' + str(result))

    print('Numero de ocorrencias no texto:')
    y = texto.count(encontrar)
    print(y)

# Obs: Colocar lista e valor pedido em vermelho...
    RED = "\033[1;31m"
    z = (RED + encontrar)
    print(texto and z)

else:
    RED = "\033[1;31m"
    print(RED + '\033[1mNão está na lista!\033[0m')

