def lista_cliente(nome):
    arquivo = open('cliente.txt', 'r')
    lista1 = []
    lista1.append(arquivo)
    lista1 = arquivo.split()
    arquivo.close()

def lista_endereco(endereco):
    arquivo = open('endereco.txt', 'r')
    lista2 = []
    lista2.append(arquivo)
    lista2 = arquivo.split()
    arquivo.close()

def lista_codigo(codigo):
    arquivo = open('codigo.txt', 'r')
    lista3 = []
    lista3.append(arquivo)
    lista3 = arquivo.split()
    arquivo.close()

#/

def gravar_cliente(nome):
    arquivo = open('cliente.txt', 'a')
    arquivo.write(nome + ' ')
    arquivo.close()

def gravar_endereco(endereco):
    arquivo = open('endereco.txt', 'a')
    arquivo.write(endereco + ' ')
    arquivo.close()

def gravar_codigo(codigo):
    arquivo = open('codigo.txt', 'a')
    arquivo.write(codigo + ' ')
    arquivo.close()

#/

def incluir_cliente():
    nome = input('Nome: ')
    gravar_cliente(nome)

def incluir_endereco():
    endereco = input('Endereco: ')
    gravar_endereco(endereco)

def incluir_codigo():
    codigo = input('Codigo: ')
    gravar_codigo(codigo)

#/

def consultar_cliente(texto):
    __import__(lista_cliente)
    __import__(lista_endereco)
    __import__(lista_codigo)
    x = 0
    for z in lista1, lista2, lista3:
        print('Cliente: ' + lista1[x] + ', endereco:' + lista2[x] + ', codigo: ' + lista3[x])
        x += 1

    print('Cliente: ' + texto1 + ',endereco: ' + texto2 + ',codigo: ' + texto3)

def alterar_cliente(nome, lista1):
    alterar = input('Nome que deseja alterar: ')
    novo = input('Novo nome: ')
    __import__(lista_cliente)
    for index, palavra in enumerate(lista1):
        if palavra == alterar:
            lista1[index] = novo
    separar = ' '.join(lista1)
    arquivo = open('cliente.txt', 'a')
    arquivo.write(separar)

def excluir_cliente(nome, lista1):
    excluir = input('Nome que deseja excluir: ')
    __import__(lista_cliente)
    lista1.remove(excluir)
    separar = ' '.join(lista1)
    arquivo = open('cliente.txt', 'a')
    arquivo.write(separar)
    arquivo.close()

if __name__ == '__main__':
    opcao = 1
    while opcao != 5:
        print('1 - Incluir')
        print('2 - Consultar')
        print('3 - Alterar')
        print('4 - Excluir')
        print('5 - Sair')
        opcao_selecionada = input('Escolha a opcao: ')
        if opcao_selecionada == '1':
            incluir_cliente()
            incluir_endereco()
            incluir_codigo()

        elif opcao_selecionada == '2':
            consultar_cliente('texto')

        elif opcao_selecionada == '3':
            alterar_cliente()

        elif opcao_selecionada == '4':
            excluir_cliente()
            
        try:
            opcao = int(opcao_selecionada)
            if opcao > 5:
                print('Selecione uma opção:')

        except:
            print('Selecione uma opção:')