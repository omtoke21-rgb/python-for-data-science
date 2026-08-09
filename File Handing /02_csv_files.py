# CSV File Handling

import csv

students = [
    ["Name", "Marks"],
    ["Om", 85],
    ["Ojas", 78],
    ["Arjun", 91]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
