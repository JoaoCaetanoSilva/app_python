clientes = []
nome = ''
endereco = ''
codigo = 0

continuar = "S"

while (continuar == "S"):
    codigo += 1

    nome = input('digite o nome: ')
    endereco = input('digite o endereco: ')

    cliente = []
    cliente.append(codigo)
    cliente.append(nome)
    cliente.append(endereco)
    clientes.append(cliente)

    continuar = input("Deseja incluir novo cliente: ")

for cliente in clientes:
    print('Codigo: ' + cliente[0] + 'Nome: ' + cliente[1] + "Endereco: " + cliente[2])
