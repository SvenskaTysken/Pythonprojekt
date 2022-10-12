student = ("Erik",20,"man")

print(student.count("Erik"))
print(student.index("man"))

for x in student:
    print(x)

if "Erik" in student:
    print("Erik är här")