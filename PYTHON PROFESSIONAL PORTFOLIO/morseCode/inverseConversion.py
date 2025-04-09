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