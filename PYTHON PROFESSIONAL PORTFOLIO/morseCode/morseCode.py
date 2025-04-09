MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

def text_to_morse(text):
    """Converte texto em código Morse."""
    morse_code = ''
    for char in text.upper():
        if char != ' ':
            morse_code += MORSE_CODE_DICT.get(char, '') + ' '
        else:
            morse_code += '  '  # Espaço entre palavras
    return morse_code.strip()

def morse_to_text(morse_code):
    """Converte código Morse em texto."""
    reverse_morse_dict = {v: k for k, v in MORSE_CODE_DICT.items()} # Invertendo dicionário.
    words = morse_code.split('  ')
    text = ''
    for word in words:
        chars = word.split(' ')
        for char in chars:
            text += reverse_morse_dict.get(char, '')
        text += ' '
    return text.strip()

while True:
    print("\nOpções:")
    print("1. Texto para Morse")
    print("2. Morse para Texto")
    print("3. Sair")

    choice = input("Escolha uma opção: ")

    if choice == '1':
        text = input("Digite o texto: ")
        print("Código Morse:", text_to_morse(text))
    elif choice == '2':
        morse = input("Digite o código Morse: ")
        print("Texto:", morse_to_text(morse))
    elif choice == '3':
        break
    else:
        print("Opção inválida.")