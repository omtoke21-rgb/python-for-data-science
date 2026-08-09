# Text File Handling

file_name = "sample.txt"

with open(file_name, "w") as file:
    file.write("Python for Data Science\n")
    file.write("Learning data analysis with Python.\n")

with open(file_name, "r") as file:
    content = file.read()

print(content)
