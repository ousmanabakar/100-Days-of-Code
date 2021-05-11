import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

dict_data = {row.letter: row.code for (index, row) in data.iterrows()}
print(dict_data)

while True:
    users_input = input("Enter a word: ").upper()
    try:
        output_list = [dict_data[letter] for letter in users_input]
    except KeyError:
        print("Sorry, enter only letters in the alphabet please")
    else:
        print(output_list)
        break











