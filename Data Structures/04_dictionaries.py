# Dictionaries

student = {
    "name": "Om",
    "branch": "AI&DS",
    "year": 3,
    "cgpa": 8.5
}

print("Student Name:", student["name"])
print("Branch:", student["branch"])
print("Year:", student["year"])
print("CGPA:", student["cgpa"])

student["skills"] = ["Python", "SQL", "Pandas"]

print("\nUpdated Student:")
print(student)
