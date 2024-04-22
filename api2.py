import requests

respuesta = requests.get('https://fakerapi.it/api/v1/places?_quantity=1')

if respuesta.status_code == 200:
    datos = respuesta.json()
    
    lugar = datos['data'][0]
    print("Nombre del lugar:", lugar['name'])
    print("Dirección:", lugar['address'])
    print("Ciudad:", lugar['city'])
    print("País:", lugar['country'])
else:
    print("Error al hacer la solicitud:", respuesta.status_code)
