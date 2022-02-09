def gravar_cliente(codigo, nome, endereco):
    arquivo = open('cliente.txt', 'a')
    arquivo.write(codigo + ';' + nome + ';' + endereco + '\n')
    arquivo.close()


def incluir_cliente():
    nome = input('Nome: ')
    endereco = input('Endereco: ')
    codigo = input('Codigo: ')
    gravar_cliente(codigo, nome, endereco)

def consultar_cliente(nome):
    print('Incluindo cliente:', nome)

def alterar_cliente(nome):
    print('Incluindo cliente:', nome)

def excluir_cliente(nome):
    print('Incluindo cliente:', nome)


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

        elif opcao_selecionada == '2':
            consultar_cliente('Consultar:')

        elif opcao_selecionada == '3':
            alterar_cliente('Consultar:')

        elif opcao_selecionada == '4':
            excluir_cliente('Alterar:')
            
        try:
            opcao = int(opcao_selecionada)
            if opcao > 5:
                print('Selecione uma opção.')

        except:
            print('Selecione uma opção.')