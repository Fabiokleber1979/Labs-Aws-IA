import requests

def consultar_moeda():
    moeda = input("Digite o código da moeda (ex: USD, EUR): ").upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()

        chave = f"{moeda}BRL"
        if chave not in dados:
            print("Moeda não encontrada.")
            return

        info = dados[chave]
        print(f"Moeda: {moeda}/BRL")
        print(f"Valor atual: R$ {info['bid']}")
        print(f"Máxima: R$ {info['high']}")
        print(f"Mínima: R$ {info['low']}")
        print(f"Última atualização: {info['create_date']}")

    except Exception as e:
        print("Falha ao consultar a cotação da moeda.")

# Teste
consultar_moeda()
