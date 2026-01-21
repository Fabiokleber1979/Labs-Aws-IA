def calcular_preco_final():
    preco = float(input("Digite o preço do produto: R$ "))
    desconto = float(input("Digite o percentual de desconto (%): "))

    valor_desconto = preco * (desconto / 100)
    preco_final = preco - valor_desconto

    print(f"Preço final com desconto: R$ {preco_final:.2f}")

# Teste
calcular_preco_final()
