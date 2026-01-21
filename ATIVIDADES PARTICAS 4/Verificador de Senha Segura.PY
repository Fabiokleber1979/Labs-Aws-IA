def verificar_senha():
    senha = input("Digite uma senha: ")

    if len(senha) < 8:
        print("Senha inválida: deve ter pelo menos 8 caracteres.")
        return

    if not any(char.isdigit() for char in senha):
        print("Senha inválida: deve conter pelo menos um número.")
        return

    print("Senha válida!")

# Teste
verificar_senha()
