import requests
from json import loads, dumps






def request_get(url, headers = {}, payload = {}):
    return loads(requests.get(url, headers = headers, data = dumps(payload)).text)

def request_post(url, headers = {}, payload = {}):
    return loads(requests.post(url, headers = headers, data=dumps(payload)).text)

def request_put(url, headers = {}, payload = {}):
    return loads(requests.put(url = url, headers = headers, data = dumps(payload)).text)

def request_delete(url, headers = {}):
    return requests.delete(url = url, headers = headers)







if __name__ == '__main__':
    url = "https://reqres.in/api/users"
    print(request_get(url))

    usuario = {
    "name": "morpheus",
    "job": "leader"
    }
    print(request_post(url, payload=usuario))

    print(request_delete("https://reqres.in/api/users/1"))



