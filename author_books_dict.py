authors_and_books = {
    "Jane Austen": "Pride and Prejudice",
    "Charles Dickens": "Great Expectations",
    "Ernest Hemingway": "The Old Man and the Sea",
    "George Orwell": "1984",
    "Harper Lee": "To Kill a Mockingbird",
    "J.K. Rowling": "Harry Potter and the Sorcerer's Stone",
    "William Shakespeare": "Romeo and Juliet",
    "Gabriel García Márquez": "One Hundred Years of Solitude"
}

# Print the entire dictionary
print(authors_and_books)

# Access and print the book of the 5th author
print("Book of the 5th author:", authors_and_books["Harper Lee"])

# Update the book of the 7th author
authors_and_books["William Shakespeare"] = "Hamlet"

# Delete the 6th author from the dictionary
del authors_and_books["J.K. Rowling"]

# Print the last key-value pair in the dictionary
last_author_book = list(authors_and_books.items())[-1]
print("Last key-value pair:", last_author_book)
