software_companies = {
    "Microsoft": "Redmond, Washington, United States",
    "Google": "Mountain View, California, United States",
    "Apple": "Cupertino, California, United States",
    "Amazon": "Seattle, Washington, United States",
    "Facebook": "Menlo Park, California, United States",
    "Oracle": "Austin, Texas, United States",
    "IBM": "Armonk, New York, United States",
    "SAP": "Walldorf, Germany",
    "Salesforce": "San Francisco, California, United States",
    "Adobe": "San Jose, California, United States"
}

# Print the entire dictionary
print(software_companies)

# Access and print the headquarters of the 3rd company
print("Headquarters of the 3rd company:", software_companies["Apple"])

# Update the headquarters of the 8th company
software_companies["SAP"] = "Walldorf, Germany (Headquarters); Newtown Square, Pennsylvania, United States (North American Headquarters)"

# Delete the 9th company from the dictionary
del software_companies["Salesforce"]

# Print the last key-value pair in the dictionary
last_company = list(software_companies.items())[-1]
print("Last key-value pair:", last_company)