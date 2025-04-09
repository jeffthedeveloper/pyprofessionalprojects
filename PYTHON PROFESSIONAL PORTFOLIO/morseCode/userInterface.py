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