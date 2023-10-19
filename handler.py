import json
import requests

def ayudantia_serverless(event, context):

    # Obtenemos la ip desde el event
    ip = event['queryStringParameters']['ip']

    # Creamos la URL para hacer la consulta
    URL = f"http://ip-api.com/json/{ip}"

    # Hacemos la consulta a la API
    response = requests.get(URL)

    # Obtenemos el JSON de la respuesta
    json_return = response.json()

    # Creamos el body de la respuesta
    body = {
        'status': 200,
        'data': json_return
    }

    # Retornamos la respuesta
    return body
