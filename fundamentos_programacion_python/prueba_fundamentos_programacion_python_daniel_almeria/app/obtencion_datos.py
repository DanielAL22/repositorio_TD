import app.api_manager as api_manager


URL = "https://aves.ninjas.cl/api/birds"

def obtener_photos(index:int):
    response = api_manager.request_get(URL)[index]['images']['full']
    return response

def obtener_name_spanish(index:int):
    response = api_manager.request_get(URL)[index]['name']['spanish']
    return response

def obtener_name_english(index:int):
    response = api_manager.request_get(URL)[index]['name']['english']
    return response






if __name__ == '__main__':
    url = "https://aves.ninjas.cl/api/birds"
    print(obtener_photos(index = 0))
    print(obtener_name_spanish(index = 0))
    print(obtener_name_english(index = 0))

