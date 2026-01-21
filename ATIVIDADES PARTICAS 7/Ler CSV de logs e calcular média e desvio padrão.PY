import pandas as pd

def analisar_logs_csv():
    arquivo = input("Digite o nome do arquivo CSV de logs: ")
    try:
        df = pd.read_csv(arquivo)
        media = df["tempo_execucao"].mean()
        desvio = df["tempo_execucao"].std()
        print(f"Média do tempo de execução: {media:.2f}")
        print(f"Desvio padrão do tempo de execução: {desvio:.2f}")
    except Exception as e:
        print("Erro ao ler o arquivo CSV ou coluna não encontrada.")

# Teste
analisar_logs_csv()
