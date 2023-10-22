import configuration
import requests
import data


def post_new_user(body):   # создание пользователя
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.user_headers)  # а здесь заголовки

response = post_new_user(data.user_body);
response.json()["authToken"]

def post_new_client_kit(body):   # создание личного набора для пользователя
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.kits_headers)  # а здесь заголовки











