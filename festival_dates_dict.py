festivals = {
    "Christmas": "December 25th",
    "New Year's Day": "January 1st",
    "Valentine's Day": "February 14th",
    "Easter": "Varies (typically in March or April)",
    "Halloween": "October 31st",
    "Thanksgiving Day": "Fourth Thursday of November",
    "Independence Day (USA)": "July 4th",
    "Mother's Day": "Second Sunday of May",
    "Father's Day": "Third Sunday of June",
    "Labor Day": "First Monday of September"
}

# Print the entire dictionary
print(festivals)

# Access and print the date of the 3rd festival
print("Date of the 3rd festival:", festivals["Valentine's Day"])

# Update the date of the 7th festival
festivals["Independence Day (USA)"] = "July 4th"  # This is already correct

# Delete the 5th festival from the dictionary
del festivals["Halloween"]

# Print the last key-value pair in the dictionary
last_festival = list(festivals.items())[-1]
print("Last key-value pair:", last_festival)
