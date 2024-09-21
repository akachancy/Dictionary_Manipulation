apps = {
    "TikTok": 4.6,
    "Instagram": 4.8,
    "WhatsApp": 4.5,
    "Facebook": 4.3,
    "YouTube": 4.7,
    "Snapchat": 4.4,
    "Twitter": 4.2,
    "Zoom": 4.1,
    "Netflix": 4.9,
    "Spotify": 4.7
}

# Print the entire dictionary
print(apps)

# Access and print the rating of the 6th app
print("Rating of the 6th app:", apps["Snapchat"])

# Update the rating of the 8th app
apps["Zoom"] = 4.2

# Delete the 9th app from the dictionary
del apps["Netflix"]

# Print the last key-value pair in the dictionary
last_app = list(apps.items())[-1]
print("Last key-value pair:", last_app)
