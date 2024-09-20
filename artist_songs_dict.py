artists = {
    "Taylor Swift": "Cruel Summer",
    "Ed Sheeran": "Shape of You",
    "Billie Eilish": "Bad Guy",
    "The Weeknd": "Blinding Lights",
    "Harry Styles": "As It Was",
    "Doja Cat": "Say So",
    "Olivia Rodrigo": "Drivers License",
    "Bad Bunny": "Me Porto Bonito"
}

# Print the entire dictionary
print(artists)

# Access and print the top song of the 3rd artist
print("Top song of the 3rd artist:", artists["Billie Eilish"])

# Update the top song of the 6th artist
artists["Doja Cat"] = "Woman"

# Delete the 7th artist from the dictionary
del artists["Olivia Rodrigo"]

# Print the last key-value pair in the dictionary
last_artist = list(artists.items())[-1]
print("Last key-value pair:", last_artist)