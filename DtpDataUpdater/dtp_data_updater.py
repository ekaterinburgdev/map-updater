from __future__ import annotations
import json
import requests
from datetime import datetime

from Common.strapi_requests import strapi_login, post_new_object


def download_file():
    response = requests.get('http://cms.dtp-stat.ru/media/opendata/sverdlovskaia-oblast.geojson')
    return response.json()


def parse_dtp(mm=None, yyyy=None, filename=None):
    endpoint = 'https://map.ekaterinburg.design/api/dtps'
    token = strapi_login()['jwt']
    object_to_file = []
    if mm is None:
        mm = datetime.now().month - 1
    if yyyy is None:
        if mm == 12:
            yyyy = datetime.now().year - 1
        else:
            yyyy = datetime.now().year
    if filename is not None:
        with open(filename, encoding='utf-8') as file:
            all_dtps = json.load(file)
            filter_data(all_dtps, yyyy, mm, object_to_file)
    else:
        res = download_file()['features']
        filter_data(res, yyyy, mm, object_to_file)

    for obj in object_to_file:
        res = post_new_object(token, obj, endpoint)


def filter_data(all_dtps, yyyy, mm, object_to_file):
    for dtp in all_dtps:
        if dtp["properties"]["region"] is not None:
            if "Екатеринбург" in dtp["properties"]["region"] and f'{yyyy}-{mm}' in dtp["properties"]["datetime"]:
                dtp_obj = {}
                dtp_obj = dtp['properties']
                dtp_obj['geometry'] = dtp['geometry']
                object_to_file.append(dtp_obj)


if __name__ == "__main__":
    parse_dtp()
