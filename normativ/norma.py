
import csv
import pickle

# with open("student.txt", "w") as fayl:
#     fayl.write("John Smith - 85\n")
#     fayl.write("Emily Johnson - 90\n")
#     fayl.write("Michael Brown - 78\n")
#     fayl.write("Sarah Davis - 92\n")
#     fayl.write("David Wilson - 69\n")


# student=[]
# with open("student.txt", "r") as fayl:
#     data = fayl.readlines()
#     for i in data:
#         student.append(i.rstrip())
#         print(i.rstrip())
#
#
# s = []
# for i in student:
#     a = i.split(" - ")
#     if int(a[1])<80:
#         s.append(f"{a[0]} - {int(a[1])+5}\n")
#     else:
#         s.append(f"{a[0]} - {int(a[1])}\n")
#
# print(s)
#
# with open("student1.txt", "w") as fayl:
#     for i in s:
#         fayl.write(i)
#         print(i)

#2
import csv
data1 = [
    {"name" : "John Smith",  "grade" : "85"},
    {"name" : "Emily Johnson", "grade" : "90"},
    {"name" : "Michael Brown", "grade" : "78"},
    {"name" : "Sarah Davis", "grade" : "92"},
    {"name" : "David Wilson", "grade" : "69"}
]


# with open("student.csv", "w", newline="") as file:
#     main = ["name", "grade"]
#     w = csv.DictWriter(file, fieldnames=main)
#     w.writeheader()
#     w.writerows(data1)


# with open("student.csv", "r") as file:
#     r = csv.DictReader(file)
#     for i in r:
#         if int(i.get("grade")) < 80:
#             print (f"{i.get("name")} - {int(i.get("grade"))+5}")
#         else:
#             print(f"{i.get("name")} - {int(i.get("grade"))}")



#3

# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#
#     def __str__(self):
#         return f"{self.name} - {self.grade}"
#
# student = Student("John Smith", 85)
# student1 = Student("Emily Johnson", 90)
# student2 = Student("Michail Brown", 78)
# student3 = Student("Sarah Devis", 92)
# student4 = Student("David Wilson", 69)
#
with open("student.dat", "wb") as file:
    pickle.dump(data1, file)

with open("student.dat", "rb") as file:
    a= pickle.load(file)
    print(a)


#4
import json

# student = {
#     "name" : "John Smith",
#     "grade" : 85
# }
# student1 = {
#     "name" : "Emily Johnson",
#     "grade" : 90
# }
# student2 = {
#     "name" : "Michail Broun",
#     "grade" : 78
# }
# student3 = {
#     "name" : "Sarah Devis",
#     "grade" : 92
# }
# student4 = {
#     "name" : "David Wilson",
#     "grade" : 69
# }
# with open("student.json", "w") as file:
#     json.dump(student, file, indent=4)
#     json.dump(student1, file, indent=4)
#     json.dump(student2, file, indent=4)
#     json.dump(student3, file, indent=4)
#     json.dump(student4, file, indent=4)

#
# with open("student.json", "r") as file:
#     dat1 = json.load(file)
# print(dat1)
