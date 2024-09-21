universities = {
    "Harvard": "Computer Science",
    "Stanford": "Computer Science",
    "MIT": "Electrical Engineering and Computer Science",
    "Oxford": "Law",
    "Cambridge": "Natural Sciences",
    "Yale": "Economics",
    "Berkeley": "Engineering",
    "UCLA": "Business Administration"
}

# Print the entire dictionary
print(universities)

# Access and print the course of the 3rd university
print("Course of the 3rd university:", universities["MIT"])

# Update the course of the 5th university
universities["Cambridge"] = "Mathematics"

# Delete the 7th university from the dictionary
del universities["Berkeley"]

# Print the last key-value pair in the dictionary
last_university = list(universities.items())[-1]
print("Last key-value pair:", last_university)
