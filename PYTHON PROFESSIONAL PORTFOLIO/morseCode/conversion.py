def text_to_morse(text):
    """Converte texto em código Morse."""
    morse_code = ''
    for char in text.upper():
        if char != ' ':
            morse_code += MORSE_CODE_DICT.get(char, '') + ' '
        else:
            morse_code += '  '  # Espaço entre palavras
    return morse_code.strip()