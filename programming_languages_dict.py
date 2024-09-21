programming_languages = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "C++": "Bjarne Stroustrup",
    "JavaScript": "Brendan Eich",
    "Ruby": "Yukihiro Matsumoto",
    "PHP": "Rasmus Lerdorf",
    "Swift": "Chris Lattner"
}

# Print the entire dictionary
print(programming_languages)

# Access and print the developer of the 4th programming language
print("Developer of the 4th programming language:", programming_languages["JavaScript"])

# Update the developer of the 6th programming language
programming_languages["PHP"] = "The PHP Group"

# Delete the 2nd programming language from the dictionary
del programming_languages["Java"]

# Print the last key-value pair in the dictionary
last_language = list(programming_languages.items())[-1]
print("Last key-value pair:", last_language)
