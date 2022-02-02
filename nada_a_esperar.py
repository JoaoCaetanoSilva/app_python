nomes = input('Nome dos clientes: ')
lista1 = []
lista1.append(nomes)
lista1 = nomes.split()

def atualizar_arquivo1(texto):
    arquivo = open('cliente.txt', 'w')
    arquivo.write(texto)
    atualizar_arquivo1(nomes)
    arquivo.close()

endereco = input('Endereco dos cliente: ')
lista2 = []
lista2.append(endereco)
lista2 = endereco.split()

def atualizar_arquivo2(texto):
    arquivo = open('endereco.txt', 'w')
    arquivo.write(texto)
    atualizar_arquivo2(endereco)
    arquivo.close()

codigo = input('Codigo dos clientes: ')
lista3 = []
lista3.append(codigo)
lista3 = codigo.split()

def atualizar_arquivo2(texto):
    arquivo = open('codigo.txt', 'w')
    arquivo.write(texto)
    atualizar_arquivo2(codigo)
    arquivo.close()

class Modificacao_Cliente:
    modificar = int(input('Deseja adicionar o nome de um novo cliente, exclui-lo ou altera-lo? Se sua resposta for sim. DIGITE 1. Se nao DIGITE 2: '))
    if modificar == 1:
        confirmado = int(input('Para adicionar o nome de um novo cliente digite: 2 \nPara excluir o nome do cliente digite: 3 \nPara altera-lo digite: 4: \nOpção: '))

        if confirmado == 2:
            adicionar1 = input('Nome do novo cliente: ')
            from nada_a_esperar import atualizar_arquivo1
            atualizar_arquivo1.append(adicionar1)
            print(lista1)

        if confirmado == 3:
            excluir1 = input('Nome que deseja excluir: ')
            from nada_a_esperar import atualizar_arquivo1
            atualizar_arquivo1.remove(excluir1)
            print(lista1)

        if confirmado == 4:
            alterar1 = input('Nome que deseja alterar: ')
            novo1 = input('Novo nome: ')
            from nada_a_esperar import atualizar_arquivo1
            for index, palavra in enumerate(atualizar_arquivo1):
                if palavra == alterar1:
                    lista1[index] = novo1
            print(lista1)

        else:
            ...