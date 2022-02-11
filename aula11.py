lista = [1, 10]

try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 2
    numero = lista[1]
    a = 0
    x = a
except ZeroDivisionError:
    print('Não é possivel dividir por 0')
except ArithmeticError:
    print('Erro ao realizar a operacao')
except IndexError:
    print('Não existe nada na lista nessa posicao')
except NameError:
    print('Nome nao declarado')
except Exception as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa se nao tiver excecoes no codigo')
finally:
    print('Sempre executara')
    arquivo.close()

