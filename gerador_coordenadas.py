import requests
import time

# URL do seu backend Django
# url = " https://9bb7-200-133-203-50.ngrok-free.app/usuario/receber_coordenadas"
url = "http://127.0.0.1:8000/usuario/receber_coordenadas"


# Dados que o ESP32 enviaria
dados = {
    "latitude": -23.5505,
    "longitude": -46.6333
}


for i in range(0,10000):

    time.sleep(5)
    try:
    # Fazendo uma requisição GET com os dados como parâmetros
        response = requests.get(url, params=dados)

        
        # Mostrando a respGJosta do servidor
        print("Status code:", response.status_code)
        print("Resposta do servidor:", response.text)


    except requests.exceptions.RequestException as e:
        print("Erro ao fazer a requisição:", e)



