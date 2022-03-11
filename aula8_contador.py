def contador_letras(lista):
    contador = []
    for x in lista:
        quantidade = len(x)
        contador.append(quantidade)
    return contador

if __name__ == '__main__':
    lista = ['s s']
    print(contador_letras(lista))
    # s = sum(contador_letras(lista))
    # print(s)