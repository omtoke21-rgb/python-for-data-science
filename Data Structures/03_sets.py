# Sets

python_students = {"Om", "Ojas", "Amit", "Sejal"}
sql_students = {"Om", "Amit", "Priya"}

print("Python Students:", python_students)
print("SQL Students:", sql_students)

print("Students learning both:")
print(python_students.intersection(sql_students))

print("All students:")
print(python_students.union(sql_students))
