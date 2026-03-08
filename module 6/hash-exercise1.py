# CHAPTER 6 EXERCISE 1
'''
Student Grade Lookup (Dictionary) Exercise

A teacher wants a quick way to store and look up student grades.

Create a program that:
- Stores student names and grades in a dictionary
- Lets the user choose from multiple actions:
    add/update a grade
    search a student’s grade
    print all students and grades
    loop until they select 0 (zero)

- If the student is not found, print a message

Example data
"Anna": 5
"Mikko": 4
"Sara": 3

'''

# Hint! Use a dictionary and while loop for example!



# CHAPTER 6 EXERCISE 1
"""
Student Grade Lookup (Dictionary) Exercise
"""

# CHAPTER 6 EXERCISE 1
"""
Student Grade Lookup (Dictionary) Exercise
"""

# starting data
grades = {
    "Anna": 5,
    "Mikko": 4,
    "Sara": 3
}

while True:
    print("\nStudent Grade System")
    print("1 - Add / Update grade")
    print("2 - Search student grade")
    print("3 - Print all students")
    print("0 - Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = int(input("Enter grade: "))
        grades[name] = grade
        print("Grade added/updated.")

    elif choice == "2":
        name = input("Enter student name to search: ")
        if name in grades:
            print(name, "grade is", grades[name])
        else:
            print("Student not found.")

    elif choice == "3":
        print("\nAll students and grades:")
        for name, grade in grades.items():
            print(name, ":", grade)

    elif choice == "0":
        print("Program ended.")
        break

    else:
        print("Invalid option.")


#output
"""
Student Grade System
1 - Add / Update grade
2 - Search student grade
3 - Print all students
0 - Exit
Choose an option: 3

All students and grades:
Anna : 5
Mikko : 4
Sara : 3


Student Grade System
1 - Add / Update grade
2 - Search student grade
3 - Print all students
0 - Exit
Choose an option: 2
Enter student name to search: Mikko
Mikko grade is 4


Student Grade System
1 - Add / Update grade
2 - Search student grade
3 - Print all students
0 - Exit
Choose an option: 1
Enter student name: John
Enter grade: 5
Grade added/updated.


Student Grade System
1 - Add / Update grade
2 - Search student grade
3 - Print all students
0 - Exit
Choose an option: 3

All students and grades:
Anna : 5
Mikko : 4
Sara : 3
John : 5


Student Grade System
1 - Add / Update grade
2 - Search student grade
3 - Print all students
0 - Exit
Choose an option: 0
Program ended.

"""