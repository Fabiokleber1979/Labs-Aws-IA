def classificador_idade():
    idade = int(input("Digite sua idade: "))
    if 0 <= idade <= 12:
        categoria = "Criança"
    elif 13 <= idade <= 17:
        categoria = "Adolescente"
    elif 18 <= idade <= 59:
        categoria = "Adulto"
    else:
        categoria = "Idoso"
    print(f"Você é classificado como: {categoria}")

# Teste
classificador_idade()
