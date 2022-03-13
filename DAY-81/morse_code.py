# Python program to implement Morse Code Translator

logo = """  __  __                        _____          _        _______                  _       _             
 |  \/  |                      / ____|        | |      |__   __|                | |     | |            
 | \  / | ___  _ __ ___  ___  | |     ___   __| | ___     | |_ __ __ _ _ __  ___| | __ _| |_ ___  _ __ 
 | |\/| |/ _ \| '__/ __|/ _ \ | |    / _ \ / _` |/ _ \    | | '__/ _` | '_ \/ __| |/ _` | __/ _ \| '__|
 | |  | | (_) | |  \__ \  __/ | |___| (_) | (_| |  __/    | | | | (_| | | | \__ \ | (_| | || (_) | |   
 |_|  |_|\___/|_|  |___/\___|  \_____\___/ \__,_|\___|    |_|_|  \__,_|_| |_|___/_|\__,_|\__\___/|_|   
                                                                                                       
                                                                                                       """

# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def encrypt(text):
    cipher = ""
    for char in text.upper():
        if char != " ":
            cipher += MORSE_CODE_DICT[char] + " "
        else:
            cipher += " "

    return cipher


def decrypt(text):
    decipher = ""
    citext = ""
    text += " "
    for char in text.upper():
        if char != " ":
            i = 0
            citext += char
        else:
            # if i = 1 there is a new character
            i += 1

            # if i = 2 there is a new word
            if i == 2:
                decipher += " "
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ""

    return decipher

print(logo)
a = encrypt(text="ousman")
print(a)

b = decrypt(text="--- ..- ... -- .- -. ")
print(b.title())


# if __name__ == "__main__":
#     print("This program translates words into to morse code.\n")
# words = input("Enter a word or phrase to be encoded: ")
#
#     try:
#         print(translate(words))
#     except KeyError:
# print("The word or phrase you've provided contains invalid characters - we can only convert the letters A-Z, numbers, and spaces to Morse Code in this program.")
