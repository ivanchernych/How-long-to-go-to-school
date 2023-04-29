from func import lonlat_distance
import requests
from io import BytesIO
from PIL import Image

coord = input().split(';')
coord_new = []
for el in coord:
    a, b = el.split(', ')
    coord_new.append((float(a), float(b)))
coord = coord_new

x = len(coord) // 2

res = 0

for el in range(len(coord)):
    if coord[el] == coord[-1]:
        break

    res += int(lonlat_distance(coord[el], coord[el + 1]))

delta = "0.009"
pl = ''

for i in range(len(coord)):
    hh = "{0},{1}".format(coord[i][0], coord[i][1])
    pl += f'{hh},'


ad = "{0},{1}".format(coord[x][0], coord[x][1])


map_params = {
    "ll": ad,
    "spn": ",".join([delta, delta]),
    "l": "map",
    "pt": f'{ad},pm2dgl',
    "pl": pl[:-1]
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)

print(res, 'м')

Image.open(BytesIO(
    response.content)).show()
