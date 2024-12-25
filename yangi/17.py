


class University:
    def __init__(self, name):
        self.name = name
        self.talabalar = []

    def __eq__(self, other):
        return len(u1.talabalar) == len(u2.talabalar)

    def __add__(self, other):
        if isinstance(other, University):
            new_universitet = University(f"{self.name} va {other.name}")
            new_universitet.talabalar = self.talabalar + other.talabalar
            return new_universitet
        return f"siz Universitet o"

    def __sub__(self, other):
        if isinstance((other, University)):
            universitet = University(f"{self.name} va {other.name}")
            universitet.talabalar = len(self.talabalar) - len(other.talabalar)
            return universitet
        return f"talaba ketti"

class Talaba:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades



u1 = University("TATU")
u2 = University("Turin")
u1.__add__("Aziz")
u2.__add__("Said")


print(u1-u2)
print(u2)




