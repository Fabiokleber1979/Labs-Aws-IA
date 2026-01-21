import json

def json_pessoas():
    dados = {
        "Nome": "João",
        "Idade": 28,
        "Cidade": "Camaragibe"
    }

    arquivo = "pessoa.json"

    # Salvar em JSON
    try:
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)
        print(f"Arquivo {arquivo} salvo com sucesso!")
    except Exception as e:
        print("Falha ao salvar o arquivo JSON.")
        return

    # Ler JSON
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            dados_lidos = json.load(f)
        print("Dados lidos do JSON:")
        print(dados_lidos)
    except FileNotFoundError:
        print("Erro: arquivo JSON não encontrado.")
    except Exception as e:
        print("Erro ao ler o arquivo JSON.")

# Teste
json_pessoas()
