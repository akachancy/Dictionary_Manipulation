companies = {
    "Apple": "Tim Cook",
    "Google": "Sundar Pichai",
    "Microsoft": "Satya Nadella",
    "Amazon": "Andy Jassy",
    "Tesla": "Elon Musk",
    "Meta": "Mark Zuckerberg",
    "Netflix": "Reed Hastings",
    "Intel": "Pat Gelsinger",
    "Salesforce": "Marc Benioff",
    "IBM": "Arvind Krishna"
}

# Print the entire dictionary
print(companies)

# Access and print the CEO of the 6th company
print("CEO of the 6th company:", companies["Meta"])

# Update the CEO of the 3rd company
companies["Microsoft"] = "Satya Nadella"  # This is already correct

# Delete the 9th company from the dictionary
del companies["Salesforce"]

# Print the last key-value pair in the dictionary
last_company = list(companies.items())[-1]
print("Last key-value pair:", last_company)
