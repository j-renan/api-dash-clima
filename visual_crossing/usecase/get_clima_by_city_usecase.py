import json
from datetime import datetime, timedelta

import requests

from environment import *


class GetClimaByCityUseCase:

    def __init__(self):
        self.__url_base = config.get('BASE_URL_VISUAL_CROSSING')
        self.__api_key = config.get('VISUAL_CROSSING_API_KEY')
        self.__today = datetime.now().strftime('%Y-%m-%d')
        self.__end_date = datetime.now() + timedelta(days=6)

    def execute(self, city: str):
        url = self.__url_base + city + ',UK/' + self.__today + '/' + self.__end_date.strftime('%Y-%m-%d') + '?key=' + self.__api_key
        response = requests.request("GET", url)
        if response.status_code == requests.codes.ok:
            location = json.loads(response.text).get('resolvedAddress')
            previsao_sete_dias = json.loads(response.text).get('days')
            current_data = json.loads(response.text).get('currentConditions')
            dados_clima = {
                'data': self.__today,
                'hora': current_data['datetime'] if current_data else None,
                'cidade': location,
                'temperatura': self.__fahrenheit_to_celsius(current_data['temp']) if current_data else None,
                'umidade': current_data['humidity'] if current_data else None,
                'vento': self.__mph_to_kmph(current_data['windspeed']) if current_data else None,
                'precipitacao': current_data['precip'] if current_data else None,
                'icon': current_data['icon'] if current_data else None,
                'previsao': []
            }
            for dia in previsao_sete_dias:
                dados_clima['previsao'].append({
                    'data': datetime.strptime(dia['datetime'], "%Y-%m-%d").date().strftime('%d/%m/%Y'),
                    'temperatura_max': self.__fahrenheit_to_celsius(dia['tempmax']),
                    'temperatura_min': self.__fahrenheit_to_celsius(dia['tempmin']),
                    'umidade': dia['humidity'],
                    'vento': self.__mph_to_kmph(dia['windspeed']),
                    'precipitacao': dia['precip'],
                    'icon': dia['icon']
                })
            print('dados_clima---------------- ', json.dumps(dados_clima, indent=4), flush=True)
            return dados_clima
        else:
            return {"message": "Erro ao buscar dados"}

    def __fahrenheit_to_celsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius

    def __mph_to_kmph(self, mph):
        kmph = mph * 1.60934
        return kmph
