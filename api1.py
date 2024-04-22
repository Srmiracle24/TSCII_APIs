import requests

respuesta = requests.get('https://fakerapi.it/api/v1/books?_quantity=1')

if respuesta.status_code == 200:
    datos = respuesta.json()
    
    libro = datos['data'][0]
    print("Título del libro:", libro['title'])
    print("Autor:", libro['author'])
    print("Género:", libro['genre'])
    print("ISBN:", libro['isbn'])
else:
    print("Error al hacer la solicitud:", respuesta.status_code)
