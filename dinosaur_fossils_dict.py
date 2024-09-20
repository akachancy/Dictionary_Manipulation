dinosaurs = {
    "Tyrannosaurus Rex": "North America",
    "Brachiosaurus": "North America",
    "Stegosaurus": "North America",
    "Velociraptor": "Mongolia",
    "Triceratops": "North America",
    "Allosaurus": "North America",
    "Spinosaurus": "Egypt and Morocco"
}

# Print the entire dictionary
print(dinosaurs)

# Access and print the location of the 4th dinosaur's fossils
print("Location of the 4th dinosaur's fossils:", dinosaurs["Velociraptor"])

# Update the location of the 2nd dinosaur's fossils
dinosaurs["Brachiosaurus"] = "East Africa"

# Delete the 6th dinosaur from the dictionary
del dinosaurs["Allosaurus"]

# Print the last key-value pair in the dictionary
last_dinosaur = list(dinosaurs.items())[-1]
print("Last key-value pair:", last_dinosaur)