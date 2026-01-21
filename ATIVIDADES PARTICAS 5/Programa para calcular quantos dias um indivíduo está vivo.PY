from datetime import datetime

def calcular_dias_vivo():
    data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    dia, mes, ano = map(int, data_nascimento.split("/"))
    nascimento = datetime(ano, mes, dia)

    hoje = datetime.now()
    dias_vivo = (hoje - nascimento).days

    print(f"Você está vivo há {dias_vivo} dias.")

# Teste
calcular_dias_vivo()
