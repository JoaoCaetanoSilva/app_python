numero1 = int(input('Entre com o numero 1: '))
numero2 = int(input('Entre com o numero 2: '))

class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

if __name__=='__main__':
    calculadora = Calculadora(numero1, numero1)
    print('Soma: {}'.format(calculadora.soma()))
    print('Subtracao: {}'.format(calculadora.subtracao()))
    print('Multiplicacao: {}'.format(calculadora.multiplicacao()))
    print('Divisao: {}'.format(calculadora.divisao()))



