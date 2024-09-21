software_programs = {
    "Microsoft Office": "365",
    "Adobe Photoshop": "24.3",
    "Blender": "3.6",
    "Figma": "11.2",
    "Canva": "2.0",
    "GIMP": "3.0"
}

# Print the entire dictionary
print(software_programs)

# Access and print the version of the 4th software
print("Version of the 4th software:", software_programs["Figma"])

# Update the version of the 2nd software
software_programs["Adobe Photoshop"] = "24.4"

# Delete the 5th software from the dictionary
del software_programs["Canva"]

# Print the last key-value pair in the dictionary
last_software = list(software_programs.items())[-1]
print("Last key-value pair:", last_software)
