#!/usr/bin/python3

if __name__ == '__main__':
    # Initialize an empty list to store students' information
    students = []

    # Get the number of students
    n = int(input())

    # Populate the students list with name and score information
    for _ in range(n):
        name = input()
        score = float(input())
        students.append([name, score])

    # Find the second lowest grade
    second_lowest_grade = sorted(set(score for name, score in students))[1]

    # Filter students with the second lowest grade and sort them alphabetically
    result_students = sorted([name for name, score in students if score == second_lowest_grade])

    # Print each student's name on a new line
    for student in result_students:
        print(student)
