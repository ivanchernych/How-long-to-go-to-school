from func import lonlat_distance
from getting import getting
import requests

address_school = input()
address_home = input()


geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"


geocoder_params_school = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": address_school,
    "format": "json"}

response_school = requests.get(geocoder_api_server, params=geocoder_params_school)
print(response_school.url)


geocoder_params_home = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": address_home,
    "format": "json"}

response_home = requests.get(geocoder_api_server, params=geocoder_params_home)
print(response_home.url)

tompony_school = getting(response_school)
tompony_home = getting(response_home)

print(tompony_school, tompony_home)

print(int(lonlat_distance(tompony_school, tompony_home)), 'м')

