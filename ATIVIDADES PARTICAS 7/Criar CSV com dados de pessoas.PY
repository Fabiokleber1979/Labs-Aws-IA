import pandas as pd

def criar_csv_pessoas():
    dados = {
        "Nome": ["Ana", "Carlos", "Maria"],
        "Idade": [25, 30, 22],
        "Cidade": ["Recife", "São Paulo", "Rio de Janeiro"]
    }
    df = pd.DataFrame(dados)

    arquivo = input("Digite o nome do arquivo CSV para salvar: ")
    try:
        df.to_csv(arquivo, index=False)
        print(f"Arquivo {arquivo} salvo com sucesso!")
    except Exception as e:
        print("Falha ao salvar o arquivo CSV.")

# Teste
criar_csv_pessoas()
