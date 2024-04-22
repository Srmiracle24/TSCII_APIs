import requests

respuesta = requests.get('https://fakerapi.it/api/v1/addresses?_quantity=1')

if respuesta.status_code == 200:
    datos = respuesta.json()
    
    direccion = datos['data'][0]
    print("Dirección:", direccion['address'])
    print("Ciudad:", direccion['city'])
    print("Código Postal:", direccion['zipcode'])
    print("País:", direccion['country'])
else:
    print("Error al hacer la solicitud:", respuesta.status_code)
