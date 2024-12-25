import pickle
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"{self.name} - {self.grade}"

# student = Student("John Smith", 85)
# student1 = Student("Emily Johnson", 90)
# student2 = Student("Michail Brown", 78)
# student3 = Student("Sarah Devis", 92)
# student4 = Student("David Wilson", 69)
#
# with open("student.dat", "ab+") as file:
#     pickle.dump(student, file)
#     pickle.dump(student1, file)
#     pickle.dump(student2, file)
#     pickle.dump(student3, file)
#     pickle.dump(student4, file)
#
#     file.seek(0)
#     while True:
#         try:
#             obj = pickle.load(file)
#             print(obj)
#         except EOFError:
#             break
# t = []
with open("student.dat", "ab+") as file:
    while True:
        try:
            sa = pickle.load(file)
            print(sa)
        except EOFError:
            break

        print(sa)
    # for i in s:
    #     t.append(i)
    # print(s)