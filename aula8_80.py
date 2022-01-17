nomes = input('Nome dos clientes: ')
lista1 = []
lista1.append(nomes)
lista1 = nomes.split()

mudar1 = int(input('Deseja adicionar o nome de um novo cliente, exclui-lo ou altera-lo? Se sua resposta for sim. DIGITE 1. Se nao DIGITE 2: '))
if mudar1 == 1:
    confirmado1 = int(input('Para adicionar o nome de um novo cliente digite: 2 \nPara excluir o nome do cliente digite: 3 \nPara altera-lo digite: 4: \nOpção: '))

    if confirmado1 == 2:
        adicionar1 = input('Nome do novo cliente: ')
        lista1.append(adicionar1)
        print(lista1)

    if confirmado1 == 3:
        excluir1 = input('Nome que deseja excluir: ')
        lista1.remove(excluir1)
        print(lista1)

    if confirmado1 == 4:
        alterar1 = input('Nome que deseja alterar: ')
        novo1 = input('Novo nome: ')
        for index, palavra in enumerate(lista1):
            if palavra == alterar1:
                lista1[index] = novo1
        print(lista1)

perguntar = int(input('Deseja modificar mais alguma coisa? Se sim DIGITE 1. Se nao DIGITE 2: '))
if perguntar == 1:
# Obs: Repitir funçao, sem repetir codigo. Talvez um import...
    print(mudar1)

else:
    ...
# Fazer um for para enquanto tiver clientes na lista, printar para o usuario: Endereço do fulano de tal.
# Len
endereco = input('Endereco do/a ' + lista1[0] + ': ')
lista2 = []
lista2.append(endereco)
lista2 = endereco.split()

mudar2 = int(input('Deseja adicionar o endereco de um novo cliente, exclui-lo ou altera-lo? Se sua resposta for sim. DIGITE 1. Se nao DIGITE 2: '))
if mudar2 == 1:
    confirmado2 = int(input('Para adicionar o endereco de um novo cliente digite: 2 \nPara excluir o endereco do cliente digite: 3 \nPara altera-lo digite: 4: \nOpção: '))

    if confirmado2 == 2:
        adicionar2 = input('Endereco do novo cliente: ')
        lista2.append(adicionar2)
        print(lista2)

    if confirmado2 == 3:
        excluir2 = input('Endereco que deseja excluir: ')
        lista2.remove(excluir2)
        print(lista2)

    if confirmado2 == 4:
        alterar2 = input('Endereco que deseja alterar: ')
        novo2 = input('Novo endereco: ')
        for index, palavra in enumerate(lista2):
            if palavra == alterar2:
                lista2[index] = novo2
        print(lista2)

else:
    ...

codigo = input('Codigo dos clientes: ')
lista3 = []
lista3.append(codigo)
lista3 = codigo.split()

mudar3 = int(input('Deseja adicionar o codigo de um novo cliente, exclui-lo ou altera-lo? Se sua resposta for sim. Digite 1. Se nao DIGITE 2: '))
if mudar3 == 1:
    confirmado3 = int(input('Para adicionar o codigo de um novo cliente digite: 2 \nPara excluir o codigo do cliente digite: 3 \nPara altera-lo digite: 4: \nOpção: '))

    if confirmado3 == 2:
        adicionar3 = input('Codigo do novo cliente: ')
        lista3.append(adicionar3)
        print(lista3)

    if confirmado3 == 3:
        excluir3 = input('Codigo que deseja excluir: ')
        lista3.remove(excluir3)
        print(lista3)

    if confirmado3 == 4:
        alterar3 = input('Codigo que deseja alterar: ')
        novo3 = input('Novo nome: ')
        for index, palavra in enumerate(lista3):
            if palavra == alterar3:
                lista3[index] = novo3
        print(lista3)

else:
    ...