import requests
from dotenv import dotenv_values


config = dotenv_values(".env")


def put_object(bearer: str, data: str, id_obj: str, endpoint: str) -> dict:
    headers = dict([
        ('Accept', 'application/json'),
        ('Authorization', f'Bearer {bearer}'),
        ('Content-Type', 'application/json')])
    response = requests.put(f'{endpoint}/{id_obj}',
                            json=data,
                            headers=headers)
    return response.json()


def strapi_login():
    data = {
        "identifier": config['LOGIN'],
        "password": config['PASSWORD']
    }
    response = requests.post(f'http://51.178.191.76:1337/api/auth/local', json=data)
    return response.json()


def post_new_object(bearer: str, data: str, endpoint: str) -> dict:
    headers = dict([
        ('Accept', 'application/json'),
        ('Authorization', f'Bearer {bearer}'),
        ('Content-Type', 'application/json')
    ])
    response = requests.post(endpoint, json={"data": data},
                             headers=headers)
    return response.json()


def get_object(bearer: str, data: str, endpoint: str) -> dict:
    headers = dict([
        ('Accept', 'application/json'),
        ('Authorization', f'Bearer {bearer}'),
        ('Content-Type', 'application/json'),
    ])
    response = \
        requests.get(
            f'{endpoint}?filters[id_string][$contains]={data}&pagination[pageSize]=10000',
            headers=headers)
    return response.json()
