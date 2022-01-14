numero1 = int(input('Entre com o numero 1: '))
numero2 = int(input('Entre com o numero 2: '))

class Calculadora:
    def __init__(self, numero1, numero2):
        self.valor_a = numero1
        self.valor_b = numero2

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

# class Calculadora:
#
#     def soma(self, valor_a, valor_b):
#         return valor_a + valor_b
#
#     def subtracao(self, valor_a, valor_b):
#         return valor_a - valor_b
#
#     def multiplicacao(self, valor_a, valor_b):
#         return valor_a * valor_b
#
#     def divisao(self, valor_a, valor_b):
#         return valor_a / valor_b
#
# if __name__=='__main__':
#     calculadora = Calculadora()
#     print('Soma: {}'.format(calculadora.soma(10, 3)))
#     print('Subtracao: {}'.format(calculadora.subtracao(4, 8)))
#     print('Multiplicacao: {}'.format(calculadora.multiplicacao(5, 7)))
#     print('Divisao: {}'.format(calculadora.divisao(6, 4)))



