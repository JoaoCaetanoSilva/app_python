from aula7_televisao import Televisao
from aula7_calculadora import Calculadora
from aula8_contador import contador_letras

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora(10, 5)
    print(calculadora.soma())
    lista = ['Cachorro', 'ratos']
    print(contador_letras(lista))


