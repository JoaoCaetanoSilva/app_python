def escrever_arquivo(texto):
    # Obs: Se quiser jerar dentro do Pycharm e nao fora, basta escrever ('teste.txt', 'w')
    arquivo = open('C:/Users/Joao/PycharmProjects/teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()
def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)

if __name__ == '__main__':
   media_notas('notas.txt')
   # escrever_arquivo('Primeira linha\n')
   # aluno = 'Rafael,10,2,4,5\n'
   # atualizar_arquivo('notas.txt', aluno)
   # ler_arquivo('teste.txt')
