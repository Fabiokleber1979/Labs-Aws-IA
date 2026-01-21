import requests

def consultar_cep():
    cep = input("Digite o CEP (somente números): ")
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()

        if "erro" in dados:
            print("CEP não encontrado.")
        else:
            print(f"Logradouro: {dados['logradouro']}")
            print(f"Bairro: {dados['bairro']}")
            print(f"Cidade: {dados['localidade']}")
            print(f"Estado: {dados['uf']}")

    except Exception as e:
        print("Falha ao consultar o CEP.")

# Teste
consultar_cep()
