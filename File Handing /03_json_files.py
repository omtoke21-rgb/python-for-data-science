# JSON File Handling

import json

student = {
    "name": "Om",
    "branch": "AI&DS",
    "year": 3,
    "skills": ["Python", "SQL", "Pandas"]
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

with open("student.json", "r") as file:
    data = json.load(file)

print(data)
