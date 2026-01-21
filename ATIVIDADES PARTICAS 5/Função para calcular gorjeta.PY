def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """
    Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
    """
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

# Exemplo de uso:
valor = 200.0
porcentagem = 10
print(f"Gorjeta: R$ {calcular_gorjeta(valor, porcentagem):.2f}")
