import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
dataframe = pd.DataFrame(data)

#dict_data = {letter: code for (letter, code) in zip(dataframe.letter, dataframe.code)}

dict_data = {row.letter: row.code for (index, row) in data.iterrows()}

print(dict_data)


users_input = input("Enter a word: ").upper()
#**************************************
output_list = [dict_data[letter] for letter in users_input]
print(output_list)
#***************************************


# output_list = []
#
# for i in users_input:
#     for x in dict_data.values():
#         if i == x[0]:
#             output_list.append(x)
#
# print(output_list)







