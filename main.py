import time
import os

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',

    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.'
}


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def text_to_morse(text):
    morse_arr = []

    for char in text:
        # Space between words in Morse code is typically represented by Seven dots or three spaces.
        if char == ' ':
            morse_arr.append(' ')
        else:
            morse_arr.append(morse_code_dict[char])

    morse = ' '.join(morse_arr)

    return morse


def morse_to_text(morse_code):
    decoded_msg = ''

    # Reverse the code_morse_dict to map Morse code back to characters.
    code_morse_dict = {morse: char for char, morse in morse_code_dict.items()}

    # Split Morse code into individual words
    morse_code_words = morse_code.split('   ')

    for each_code_word in morse_code_words:
        # Split Morse words into individual letters.
        decoded_letters = [code_morse_dict[each_code_letter] for each_code_letter in each_code_word.split(' ')]
        decoded_msg += ''.join(decoded_letters)
        decoded_msg += ' '

    return decoded_msg


ascii_art = """
 ______   ______     __  __     ______         __    __     ______     ______     ______     ______    
/\\__  _\\ /\\  ___\\   /\\_\\_\\_\\   /\\__  _\\       /\\ "-./  \\   /\\  __ \\   /\\  == \\   /\\  ___\\   /\\  ___\\   
\\/_/\\ \\/ \\ \\  __\\   \\/\\/_/\\/_  \\/_/\\ \\/       \\ \\ \\-./\\ \\  \\ \\ \\/\\ \\  \\ \\  __<   \\ \\___  \\  \\ \\  __\\   
   \\ \\_\\  \\ \\_____\\   /\\_\\/\\_\\    \\ \\_\\        \\ \\_\\ \\ \\_\\  \\ \\_____\\  \\ \\_\\ \\_\\  \\/____\\  \\ \\_____\\ 
    \\/_/   \\/_____/   \\/_/\\/_/     \\/_/         \\/_/  \\/_/   \\/_____/   \\/_/ /_/   \\/_____/   \\/_____/
"""

is_active = True

while is_active:
    print(ascii_art)
    print("Welcome to the International Morse Code Converter.\nWhat do you wish to do?")
    print("1. Convert Text To Morse.\n2. Convert Morse to Text.\n3. Exit\n")
    choice = input("Your choice: ")

    if choice == '1':
        clear_console()
        print("Input Restrictions: \nLetters: A-Z \nNumbers: 0-9 \nPunctuation Marks: . , ? ! ' \" : ; - ( ) & / "
              "+ = @\n")
        secret_msg = input("Enter secret message(letters must be uppercase): ").upper()
        morse_msg = text_to_morse(secret_msg)
        print(f"\nMorse Code: {morse_msg}")
        time.sleep(2)
    elif choice == '2':
        clear_console()
        print("Input Restrictions: \nCharacter Set: Only dots(.) and dashes(-). \nSpacing: Separate characters by a "
              "space and words by three spaces.\n")
        morse_msg = input("Enter morse message: ")
        text_msg = morse_to_text(morse_msg)
        print(f"Secret Message: {text_msg}")
        time.sleep(2)
    elif choice == '3':
        clear_console()
        is_active = False
        print("Exiting...")
        time.sleep(2)
    else:
        clear_console()
        print("Warning: Invalid Choice!!!")
        time.sleep(2)
