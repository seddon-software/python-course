salaries = {
    "John" : 45000,
    "Sheila" : 48000,
    "Vivien" : 31000,
    "Roy" : 37000,
    "Ruth" : 50000
}

inverted = {}
for key, value in salaries.items():
    inverted[value] = key

print(inverted)


