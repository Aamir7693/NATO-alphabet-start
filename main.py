student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
dicta={}
#TODO 1. Create a dictionary in this format:
student_frame=pd.read_csv("nato_phonetic_alphabet.csv")
print(student_frame)
for index,row in student_frame.iterrows():
    dicta.update({row.letter:row.code})
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
result=[]
inp=input("Enter a word for generating phonetics\n")
lista=[x for x in inp]
result=[dicta[char.capitalize()] for char in lista ]

print(result)