# consulta.py

import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

def consultar_cotacao():
    api_key = os.environ.get("API_KEY")

    if not api_key:
        print("API_KEY não encontrada. Verifique o arquivo .env.")
        return

    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()

        print(f"Cotação com base no dólar americano (USD):")
        print(f"Real (BRL): {dados['conversion_rates'].get('BRL')}")
        print(f"Euro (EUR): {dados['conversion_rates'].get('EUR')}")
        print(f"Libra (GBP): {dados['conversion_rates'].get('GBP')}")
        print(f"Peso Argentino (ARS): {dados['conversion_rates'].get('ARS')}")
       

    except requests.exceptions.RequestException as e:
        print("Erro na requisição:", e)

if __name__ == "__main__":
    consultar_cotacao()
