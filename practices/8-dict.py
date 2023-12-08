#!/usr/bin/python3
'''Using a for loop to access values in a dictionary'''

mdict = {"english": 98,
         "maths": 89,
         "science": 80
         }

# number one
for values in mdict:
    print(mdict[values])

# number two 
for values in mdict.values():
    print(values)

# number three to return tuples
for subject, scores in mdict.items():
    print(f"subject = {subject} and score = {scores} ")
