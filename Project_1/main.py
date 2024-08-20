# WELCOME TO MY PYTHON SHOWCASE
# DAY 83 OF 100 DAYS OF PYTHON CODE
# This is where we take a user input and return it to the user as morse code.

# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                   'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                   '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': ' '}

user_input = input("Please enter the message you would like to change to Morse Code: \n")

morse_code = ''
for letter in user_input.upper():
    morse_code += MORSE_CODE_DICT[letter]
print(f'Your message in morse code is: {morse_code}')
