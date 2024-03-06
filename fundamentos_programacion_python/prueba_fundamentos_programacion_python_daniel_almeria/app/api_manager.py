import requests
from json import loads, dumps

url = "https://aves.ninjas.cl/api/birds"

payload = {}
headers = {}



def request_get(url, headers = {}, payload = {}):
    return loads(requests.get(url, headers = headers, data = dumps(payload)).text)





# response = requests.get(url)
# print(response)
# resultados = json.loads(response.text) #Transforma la string en una lista con objetos json (diccionarios)

# print(type(response)) #<class 'requests.models.Response'>
# print(type(response.text)) #str
# print(type(resultados)) #list
# print(type(resultados[0])) #list

if __name__ == '__main__':
    url = "https://aves.ninjas.cl/api/birds"
    print(request_get(url))

