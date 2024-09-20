companies = {
    "Apple": "Steve Jobs",
    "Microsoft": "Bill Gates",
    "Google": "Larry Page and Sergey Brin",
    "Amazon": "Jeff Bezos",
    "Facebook": "Mark Zuckerberg",
    "Tesla": "Elon Musk",
    "Netflix": "Reed Hastings and Marc Randolph",
    "Uber": "Travis Kalanick and Garrett Camp"
}

# Print the entire dictionary
print(companies)

# Access and print the founder of the 6th company
print("Founder of the 6th company:", companies["Tesla"])

# Update the founder of the 2nd company
companies["Microsoft"] = "Bill Gates and Paul Allen"

# Delete the 8th company from the dictionary
del companies["Uber"]

# Print the last key-value pair in the dictionary
last_company = list(companies.items())[-1]
print("Last key-value pair:", last_company)