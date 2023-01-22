import requests

url = 'http://51.178.191.76:1337'


def post_new_dtp_object(bearer: str, data: str) -> dict:
    headers = dict([
        ('Accept', 'application/json'),
        ('Authorization', f'Bearer {bearer}'),
        ('Content-Type', 'application/json')
    ])
    response = requests.post(f'http://51.178.191.76:1337/api/dtps', json={"data": data},
                             headers=headers)
    return response.json()


def strapi_login():
    data = {
        "identifier": 'test_user',
        "password": 'm4puser1311EKBnewSecretpass9768!g'
    }
    response = requests.post(f'{url}/api/auth/local', json=data)
    return response.json()
