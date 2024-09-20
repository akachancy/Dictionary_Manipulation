books = {
    "To Kill a Mockingbird": "Harper Lee",
    "1984": "George Orwell",
    "Pride and Prejudice": "Jane Austen",
    "The Lord of the Rings": "J.R.R. Tolkien",
    "The Great Gatsby": "F. Scott Fitzgerald",
    "Harry Potter and the Philosopher's Stone": "J.K. Rowling",
    "The Hitchhiker's Guide to the Galaxy": "Douglas Adams",
    "The Catcher in the Rye": "J.D. Salinger",
    "The Alchemist": "Paulo Coelho",
    "The Hunger Games": "Suzanne Collins",
    "The Da Vinci Code": "Dan Brown",
    "The Handmaid's Tale": "Margaret Atwood"
}

# Print the entire dictionary
print(books)

# Access and print the author of the 9th book
print("Author of the 9th book:", books["The Alchemist"])

# Update the author of the 5th book
books["The Great Gatsby"] = "Scott Fitzgerald"

# Delete the 3rd book from the dictionary
del books["Pride and Prejudice"]

# Print the last key-value pair in the dictionary
last_book = list(books.items())[-1]
print("Last key-value pair:", last_book)