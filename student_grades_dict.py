students = {
    "Student1": "B+",
    "Student2": "C-",
    "Student3": "A",
    "Student4": "B",
    "Student5": "D"
}

# Print the entire dictionary
print(students)

# Access and print the grade of the 3rd student
print("Grade of third student:", students["Student3"])

# Update the grade of the 2nd student
students["Student2"] = "A"

# Delete the entry of the 5th student
del students["Student5"]

# Print the last key-value pair in the dictionary
last_student = list(students.items())[-1]
print("Last key-value pair:", last_student)