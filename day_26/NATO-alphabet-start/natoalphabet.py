import pandas
data = pandas.read_csv('nato_phonetic_alphabet.csv')
student_data_frame = pandas.DataFrame(data)
dictionary = {}
for (index, row) in student_data_frame.iterrows():
    dictionary[row.letter] = row.code
print(dictionary)
name = input(('Enter your name: ')).upper()
# for char in name:
# dict_name = [char for char in name]
result = {}
out = []
for char in name:
    add = {char : dictionary[char]}
    out.append(add)
print(out)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

