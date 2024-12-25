import pickle

from yangi.lssn15 import talaba1

# fayl = open("data.txt")
# data = fayl.read()
# print(data)
# fayl.close()

# with open("data.txt") as fayl:
#     data = fayl.read()
#     print(data)
#
# with open("data.txt") as fayl:
#     data = fayl.readlines()
# list1 = []
# for i in data:
#     list1.append(i.rstrip())
# print(list1)

fayl = open("data.txt")
data = fayl.read()
print(data)
fayl.close()

with open("data.txt") as fayl:
    data = fayl.readlines()
print(data)

with open("data.txt") as fayl:
    list1 = []
    for i in fayl:
        list1.append(i.rstrip())
print(list1)

with open("data.txt", "a+") as fayl:
    fayl.write("1221\n")
    fayl.write("432343\n")
    fayl.seek(0)
    data = fayl.readlines()
print(data)

import pickle

class Talaba:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} talaba, {self.age} yoshi"

talaba1 = Talaba("Aziz", "22")
talaba2 = Talaba("Ali", "20")

with open("info.dat", "ab+")as fayl:
    pickle.dump(talaba1, fayl)
    pickle.dump(talaba1, fayl)

    fayl.seek(0)
    while True:
        try:
            obj = pickle.load(fayl)
            print(obj)
        except EOFError:
            break
    data = pickle.load(fayl)
print(data)