def classificador_numeros():
    pares = 0
    impares = 0

    qtd = int(input("Quantos números deseja digitar? "))

    for i in range(qtd):
        num = int(input(f"Digite o número {i+1}: "))
        if num % 2 == 0:
            pares += 1
            print(f"{num} é Par")
        else:
            impares += 1
            print(f"{num} é Ímpar")

    print(f"Total de pares: {pares}")
    print(f"Total de ímpares: {impares}")

# Teste
classificador_numeros()
