from playsound import playsound
import time
import os
import pyperclip

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


# Clear console.
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def text_to_morse(text):
    """Convert text to morse code. Return morse code."""
    morse_arr = []
    morse = ''

    not_in_dict = [char for char in text.replace(" ", "") if char not in morse_code_dict.keys()]

    if len(not_in_dict) == 0:
        for char in text:
            # Space between words in Morse code is typically represented by Seven dots or three spaces.
            if char == ' ':
                morse_arr.append(' ')
            else:
                morse_arr.append(morse_code_dict[char])

        morse = ' '.join(morse_arr)
    else:
        print(f"\nWarning: {not_in_dict} doesn't exist.")
    return morse


def morse_to_text(morse_code):
    """Convert morse code to text. Return text."""
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


def play_morse_code(text, dot_duration=0.2, sound_delay=0.1):
    """Play morse code."""
    for char in text:
        if char == ' ':
            # 3 dots for word spacing.
            time.sleep(3 * dot_duration)
        else:
            morse_char = morse_code_dict.get(char.upper())
            for dot_dash in morse_char:
                # Play a short beep for a dot.
                if dot_dash == '.':
                    playsound('dot.mp3')
                # Play a longer beep for a dash.
                elif dot_dash == '-':
                    playsound('dash.mp3')
                # Delay between characters.
                time.sleep(dot_duration)
            time.sleep(sound_delay)


ascii_art = """
 ______   ______     __  __     ______         __    __     ______     ______     ______     ______    
/\\__  _\\ /\\  ___\\   /\\_\\_\\_\\   /\\__  _\\       /\\ "-./  \\   /\\  __ \\   /\\  == \\   /\\  ___\\   /\\  ___\\   
\\/_/\\ \\/ \\ \\  __\\   \\/\\/_/\\/_  \\/_/\\ \\/       \\ \\ \\-./\\ \\  \\ \\ \\/\\ \\  \\ \\  __<   \\ \\___  \\  \\ \\  __\\   
   \\ \\_\\  \\ \\_____\\   /\\_\\/\\_\\    \\ \\_\\        \\ \\_\\ \\ \\_\\  \\ \\_____\\  \\ \\_\\ \\_\\  \\/____\\  1\\ \\_____\\ 
    \\/_/   \\/_____/   \\/_/\\/_/     \\/_/         \\/_/  \\/_/   \\/_____/   \\/_/ /_/   \\/_____/   \\/_____/
"""

is_active = True

while is_active:
    print(ascii_art)
    print("Welcome to the International Morse Code Converter.\nWhat do you wish to do?")
    print("1. Convert Text To Morse.\n2. Convert Morse to Text.\n3. Play Morse Code\n4. Exit\n")
    choice = input("Your choice: ")

    # Convert Text to Morse
    if choice == '1':
        clear_console()
        print("Input Restrictions: \nLetters: A-Z \nNumbers: 0-9 \nPunctuation Marks: '. , ? \ ' ! / ( ) & : ; = + - "
              "_ \" $ @ ")
        secret_msg = input("Enter secret message(letters must be uppercase): ").upper()
        morse_msg = text_to_morse(secret_msg)
        if morse_msg == "":
            time.sleep(2)
            continue
        else:
            print(f"\nMorse Code: {morse_msg}")

            # Copy morse code to clipboard using pyperclip.
            clip_choice = input("\nStore Morse Code in clipboard(Y/N)? ").upper()
            if clip_choice == 'Y':
                pyperclip.copy(morse_msg)
                print("Morse Code Saved...")

            # Play morse code using playsound.
            play_choice = input(f"\nPlay Morse Code(Y/N)? ").upper()
            if play_choice == 'Y':
                print("Playing...\n")
                play_morse_code(secret_msg)
            else:
                time.sleep(2)

    # Convert Morse to Text.
    elif choice == '2':
        clear_console()
        print("Input Restrictions: \nCharacter Set: Only dots(.) and dashes(-). \nSpacing: Separate characters by a "
              "space and words by three spaces.\n")
        print(f"Saved Morse Code: {pyperclip.paste()}\n")

        # Use morse code saved in clipboard.
        morse_choice = input("Use Saved Morse Code(Y/N)? ").upper()
        if morse_choice == 'Y':
            morse_msg = pyperclip.paste()
            print("Using Saved Morse Code...")
        else:
            morse_msg = input("\nEnter morse message: ")
        invalid_input = False
        for morse_sym in morse_msg:
            if morse_sym not in ['.', '-', ' ']:
                invalid_input = True
        if invalid_input:
            print("\nWarning: Invalid Input!!!")
        else:
            text_msg = morse_to_text(morse_msg)
            print(f"\nSecret Message: {text_msg}")
        time.sleep(2)

    # Play Morse Code
    elif choice == '3':
        clear_console()
        # Play morse code stored in clipboard.
        print(f"Morse Code: {pyperclip.paste()}")
        print("Playing...")
        play_morse_code(morse_to_text(pyperclip.paste()))

    # Exit.
    elif choice == '4':
        clear_console()
        is_active = False
        print("Exiting...")
        time.sleep(2)

    # To deal with bad inputs.
    else:
        clear_console()
        print("Warning: Invalid Choice!!!")
        time.sleep(2)
