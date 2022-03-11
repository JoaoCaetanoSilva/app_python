import requests

def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    # print(response.status_code)
    print(response.text)
    # print(response.json())
    # dados_cep = response.json()
    # print(dados_cep['logradouro'])
    # return dados_cep

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    response = retorna_dados_cep('09291170')
    dados_pokemon = retorna_dados_pokemon('shinx')
    print(dados_pokemon['sprites']['front_shiny'])
    response = retorna_response('https://onepieceex.net/manga-1043/')
    print(response)


