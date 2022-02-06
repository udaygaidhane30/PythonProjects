import pandas

#
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:

base_data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in base_data.iterrows()}

# print(data_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
inp_word = input("Enter a word  ").upper()
output_list = [data_dict[letter] for letter in inp_word]
print(output_list)
