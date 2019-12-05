import requests


def buscar_avatar(usuario):
    '''
    Busca o avatar de um usuário no Github

    :param usuario: str Com o nome de um usuário no gitbub
    :return: str com o link para o avatar
    '''
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']
