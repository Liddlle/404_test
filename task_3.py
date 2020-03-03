import requests
url = 'https://restcountries.eu/rest/v2/'

SG = requests.get(url + 'alpha/SG')
Viet_nam = requests.get(url + 'name/Viet%20Nam')

def get_iso(d):
    return dict([(d['name'], d['alpha2Code'])])

countries_with_iso = {}

for i in [SG, Viet_nam]:
    tmp = i.json()
    if type(tmp) == list:
        tmp = tmp[0]
    countries_with_iso.update(get_iso(tmp))

print(countries_with_iso)