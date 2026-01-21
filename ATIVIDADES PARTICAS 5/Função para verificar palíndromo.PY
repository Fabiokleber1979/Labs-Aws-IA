import string

def verificar_palindromo(texto: str) -> str:
    """
    Verifica se uma palavra ou frase é palíndromo.
    Ignora espaços e pontuação.
    """
    # Remove espaços e pontuação, e coloca em minúsculo
    texto_limpo = ''.join(ch.lower() for ch in texto if ch.isalnum())
    # Verifica se é igual ao inverso
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

# Exemplo de uso:
print(verificar_palindromo("A man a plan a canal Panama"))  # Sim
print(verificar_palindromo("Python"))  # Não
