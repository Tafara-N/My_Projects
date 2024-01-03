if __name__ == '__main__':
    # Input the number of students' records
    n = int(input())
    student_marks = {}

    # Input names and marks for each student
    for _ in range(n):
        line = input().split()
        name, marks = line[0], list(map(float, line[1:]))
        student_marks[name] = marks

    # Input the name of the student to query
    query_name = input()

    # Calculate and print the average marks for the specified student
    average_marks = sum(student_marks[query_name]) / len(student_marks[query_name])
    print("{:.2f}".format(average_marks))
