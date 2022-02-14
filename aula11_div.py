class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input('Digite a nota: '))
        print(x)
        if x > 10:
            raise InputError('A nota nao pode ser maior que 10')
        elif x < 1:
            print('Nota muito baixa.')
            raise InputError('A nota nao pode ser menor que 1')
        break
    except ValueError:
        print('Valor invalido')
