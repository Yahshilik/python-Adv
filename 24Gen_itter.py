# class MyIterator:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end
#
#     def __iter__(self):
#         # print("1")
#         return self
#
#     def __next__(self):
#         print("next")
#         if self.current >= self.end:
#             raise StopIteration("xatolik")
#         self.current += 1  # 1
#         return self.current - 1

class Universitet:
    def __init__(self, name):
        self.name = name
        self.talabalar = []

    def add_student(self, student):
        if isinstance(student, Talabalar):
            self.talabalar.append(student)

    # def __iter__(self):# 2 variant
    #     self.__iter__ = iter(self.talabalar)
    #     return self
    #
    # def __next__(self): # 2 variant
    #     return next(self.__iter__)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index == len(self.talabalar):
            raise StopIteration
        self.index +=1
        return self.talabalar[self.index -1].name

class Talabalar:
    def __init__(self, name, bosqich):
        self.name = name
        self.bosqich = bosqich


st1 = Talabalar("Ali", 2)
st2 = Talabalar("Vali", 2)
st3 = Talabalar("Alisher", 2)
st4 = Talabalar("Gani", 2)

unversitet = Universitet("TATU")
unversitet.add_student(st1)
unversitet.add_student(st2)
unversitet.add_student(st3)
unversitet.add_student(st4)

for i in unversitet:
    # print(i.name) # 2 variant
print(i)