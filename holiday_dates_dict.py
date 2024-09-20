holidays = {
    "New Year's Day": "January 1st",
    "Valentine's Day": "February 14th",
    "Easter": "Varies",
    "Independence Day (USA)": "July 4th",
    "Halloween": "October 31st",
    "Thanksgiving Day (USA)": "Fourth Thursday of November",
    "Christmas": "December 25th",
    "Mother's Day": "Second Sunday of May",
    "Father's Day": "Third Sunday of June",
    "Labor Day (USA)": "First Monday of September"
}

# Print the entire dictionary
print(holidays)

# Access and print the date of the 4th holiday
print("Date of the 4th holiday:", holidays["Independence Day (USA)"])

# Update the date of the 9th holiday
holidays["Father's Day"] = "Third Sunday of June"  # This is already correct

# Delete the 2nd holiday from the dictionary
del holidays["Valentine's Day"]

# Print the last key-value pair in the dictionary
last_holiday = list(holidays.items())[-1]
print("Last key-value pair:", last_holiday)