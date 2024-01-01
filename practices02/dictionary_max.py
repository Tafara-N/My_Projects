def maximum_mark(my_dict):
    marks = list(my_dict.values())
    max = marks[0]
    for mark in marks:
        if mark > max:
            max = mark
    subjects = list(my_dict.keys())
    for subject in subjects:
        if my_dict[subject] == max:
            return subject

def main():
    dictionary1 = {'Math': 85, 'Science': 92, 'History': 78, 'English': 88}
    result = maximum_mark(dictionary1)
    print(result)
main()
