jobs_and_salaries = {
    "Software Engineer": 100000,
    "Data Scientist": 120000,
    "Doctor": 200000,
    "Lawyer": 150000,
    "Nurse": 75000,
    "Teacher": 60000,
    "Accountant": 80000,
    "Engineer": 90000,
    "Salesperson": 70000,
    "Chef": 55000
}

# Print the entire dictionary
print(jobs_and_salaries)

# Access and print the salary of the 3rd job
print("Salary of the 3rd job:", jobs_and_salaries["Doctor"])

# Update the salary of the 7th job
jobs_and_salaries["Accountant"] = 85000

# Delete the 9th job from the dictionary
del jobs_and_salaries["Salesperson"]

# Print the last key-value pair in the dictionary
last_job_salary = list(jobs_and_salaries.items())[-1]
print("Last key-value pair:", last_job_salary)
