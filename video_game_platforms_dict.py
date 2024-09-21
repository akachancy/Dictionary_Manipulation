video_games = {
    "The Last of Us": "PlayStation 4, PlayStation 5",
    "Red Dead Redemption 2": "PlayStation 4, Xbox One, PC",
    "The Witcher 3: Wild Hunt": "PlayStation 4, Xbox One, PC, Nintendo Switch",
    "Grand Theft Auto V": "PlayStation 3, PlayStation 4, Xbox 360, Xbox One, PC",
    "God of War": "PlayStation 4, PlayStation 5",
    "Halo Infinite": "Xbox Series X/S, PC",
    "Horizon Forbidden West": "PlayStation 4, PlayStation 5",
    "Resident Evil Village": "PlayStation 5, Xbox Series X/S, PC"
}

# Print the entire dictionary
print(video_games)

# Access and print the platform of the 2nd video game
print("Platform of the 2nd video game:", video_games["Red Dead Redemption 2"])

# Update the platform of the 6th video game
video_games["Halo Infinite"] = "Xbox Series X/S, PC, Xbox One"

# Delete the 4th video game from the dictionary
del video_games["Grand Theft Auto V"]

# Print the last key-value pair in the dictionary
last_game = list(video_games.items())[-1]
print("Last key-value pair:", last_game)
