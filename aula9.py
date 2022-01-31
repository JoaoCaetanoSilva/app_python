# Obs: W = escrever, A = atualizar, R = ler
def escrever_arquivo(texto):
    diretorio = 'C:/Users/Joao/PycharmProjects/teste.txt'
    arquivo = open(diretorio, 'w')
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
    print(aluno_nota)

if __name__ == '__main__':
    media_notas('notas.txt')
    # escrever_arquivo('Primeira Linha. \n')
    # aluno = 'Isaque 2,2,3,5\n'
    # atualizar_arquivo('notas.txt', aluno)
    # # ler_arquivo('teste.txt')