albums = {
    "Born to Run" : 1975,
    "Thriller" : 1982,
    "Nevermind" : 1991,
    "The Dark Side of the Moon" : 1973,
    "Abbey Road" : 1969,
    "Back to Black" : 2006,
    "Rumours" : 1977,
    "Born This Way" : 2011,
    "21" : 2011,
    "Dookie" : 1994
}

# Print the entire dictionary
print(albums)

# Access and print the release year of the 3rd album
print("Release year of the 3rd album:", albums["Nevermind"])

# Update the release year of the 8th album
albums["Born This Way"] = 2011  # This is already correct

# Delete the 5th album from the dictionary
del albums["Abbey Road"]

# Print the last key-value pair in the dictionary
last_album = list(albums.items())[-1]
print("Last key-value pair:", last_album)
