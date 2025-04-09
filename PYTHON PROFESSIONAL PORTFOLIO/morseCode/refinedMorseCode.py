MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': ' ' #Espaço adicionado ao dicionário
}

def text_to_morse(text):
    """
    Converte uma string de texto em código Morse.

    Args:
        text (str): A string de texto a ser convertida.

    Returns:
        str: O código Morse equivalente.
    """
    morse_code = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append('')  # Lida com caracteres desconhecidos
    return ' '.join(morse_code)

def main():
    """Função principal para executar o conversor."""
    while True:
        print("\nConversor de Texto para Código Morse")
        print("1. Converter Texto")
        print("2. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            text = input("Digite o texto: ")
            morse = text_to_morse(text)
            print("Código Morse:", morse)
        elif choice == '2':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()