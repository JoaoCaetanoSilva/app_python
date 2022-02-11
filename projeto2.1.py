nomes = input('Nome dos clientes: ')
lista1 = []
lista1.append(nomes)
lista1 = nomes.split()

arquivo = open('cliente.txt', 'w')
arquivo.write(nomes)
arquivo.close()

modificar = int(input('Deseja adicionar o nome de um novo cliente, exclui-lo ou altera-lo? Se sua resposta for sim. DIGITE 1. Se nao DIGITE 2: '))
if modificar == 1:
    confirmado = int(input('Para adicionar o nome de um novo cliente digite: 2 \nPara excluir o nome do cliente digite: 3 \nPara altera-lo digite: 4: \nOpção: '))

    if confirmado == 2:
        adicionar1 = input('Nome do novo cliente: ')
        arquivo = open('cliente.txt', 'a')
        arquivo.write(' ' + adicionar1)
        arquivo.close()

    if confirmado == 3:
        excluir1 = input('Nome que deseja excluir: ')
        lista1.remove(excluir1)
        separar1 = ' '.join(lista1)
        arquivo = open('cliente.txt', 'w')
        arquivo.write(separar1)
        arquivo.close()

    if confirmado == 4:
        alterar1 = input('Nome que deseja alterar: ')
        novo1 = input('Novo nome: ')
        for index, palavra in enumerate(lista1):
            if palavra == alterar1:
                lista1[index] = novo1
        separar2 = ' '.join(lista1)
        arquivo = open('cliente.txt', 'w')
        arquivo.write(separar2)
#/
x = 0
for z in lista1:
    endereco = input('Endereco de ' + lista1[x] + ': ')
    x += 1

arquivo1 = open('endereco.txt', 'r')
arquivo1.read()
arquivo1.close()

lista2 = []
lista2.append(arquivo1)
lista2 = (arquivo1).split()

modificar = int(input('Deseja adicionar o endereco de um novo cliente, exclui-lo ou altera-lo? Se sua resposta for sim. DIGITE 1. Se nao DIGITE 2: '))
if modificar == 1:
    confirmado = int(input('Para adicionar o endereco de um novo cliente digite: 2 \nPara excluir o endereco do cliente digite: 3 \nPara altera-lo digite: 4: \nOpção: '))

    if confirmado == 2:
        adicionar1 = input('Endereco do novo cliente: ')
        arquivo = open('endereco.txt', 'a')
        arquivo.write(' ' + adicionar1)
        arquivo.close()

    if confirmado == 3:
        excluir1 = input('Endereco que deseja excluir: ')
        lista2.remove(excluir1)
        separar1 = ' '.join(lista1)
        arquivo = open('endereco.txt', 'w')
        arquivo.write(separar1)
        arquivo.close()

    if confirmado == 4:
        alterar1 = input('Endereco que deseja alterar: ')
        novo1 = input('Novo endereco: ')
        for index, palavra in enumerate(lista2):
            if palavra == alterar1:
                lista2[index] = novo1
        separar2 = ' '.join(lista1)
        arquivo = open('endereco.txt', 'w')
        arquivo.write(separar2)
