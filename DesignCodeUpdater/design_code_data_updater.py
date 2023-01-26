import requests

from Common.strapi_requests import strapi_login, get_object, put_object, post_new_object

endpoint = 'https://map-api.ekaterinburg.io/api/design-codes'
token = strapi_login()['jwt']
response = requests.get('https://map.ekaterinburg.design/api/map')
data = response.json()
for code_object in data:
    code_object['geometry'] = {'type': 'Point', 'coordinates': [code_object['coords'][1], code_object['coords'][0]]}
    code_object['geometry']['type'] = 'Point'
    code_object['id_string'] = code_object['id']
    del code_object['id']
    data_from_strapi = get_object(token, code_object['id_string'], endpoint)["data"]
    if data_from_strapi:
        put_object(token, code_object, data_from_strapi[0]['id'], endpoint)
    else:
        post_new_object(token, code_object, endpoint)
