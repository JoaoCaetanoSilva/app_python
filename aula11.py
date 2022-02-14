lista = [1, 10]

arquivo = open('teste.txt', 'r')
try:
    texto = arquivo.read()
    divisao = 10 / 2
    numero = lista[1]
    a = 0
    x = a
    arquivo.close()
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
    print('Fechando arquivo')
    arquivo.close()

