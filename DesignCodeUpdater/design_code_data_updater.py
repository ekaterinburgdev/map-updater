import requests

from DesignCodeUpdater.strapi_requests import put_object, get_object, strapi_login, post_new_object

response = requests.get('https://map.ekaterinburg.design/api/map')
data = response.json()
for code_object in data:
    code_object['geometry'] = {'type': 'Point', 'coordinates': [code_object['coords'][1], code_object['coords'][0]]}
    code_object['geometry']['type'] = 'Point'
    code_object['id_string'] = code_object['id']
    del code_object['id']
    token = strapi_login()['jwt']
    data_from_strapi = get_object(token, code_object['id_string'])["data"]
    if data_from_strapi:
        put_object(token, code_object, data_from_strapi[0]['id'])
    else:
        post_new_object(token, code_object)

