# class LibraryItem:
#
#
# class Book:
#     def __init__(self, ISBN, name, subject, dds_number, authors=[]):
#         self.ISBN= ISBN
#         self.name= name
#         self.subject= subject
#         self.dds_number= dds_number
#         self.authors= authors
#     def get_info(self):
#         return f"{self.name, self.subject}"
#
#     def get_name(self):
#         return self.name
#
#     def get_subject(self):
#         return self.subject
#
#     def get_dds_number(self):
#         return self.dds_number
#
#     def get_authors(self):
#         return self.authors
#
# class Catalog:
#     def __init__(self, name):
#         self.name = name
#         self.books = []
#
#     def search(self, name="", author=""):
#         if name:
#             book = []
#             for i in self.books:
#                 if i.name == name:
#                     book.append(i)
#             if book:
#                 for i in book:
#                     print(f"bu kitob {i.dds_number} da joylashgan")
#             else:
#                 print("topilmadi")
#         elif author:
#             book = []
#             for i in self.books:
#                 if i.author == author:
#                     book.append(i)
#             if book:
#                 for i in book:
#                     print(f"bu kitob {i.dds_number} da joylashgan")
#             else:
#                 print("author topilmadi")
#
#
#
#     def add_book(self,book: Book):
#         if isinstance(book, Book):
#             self.books.append(book)
#             print(f"sizning {book.get_info()} qoshildi")
#         else:
#             print("siz Book classiga tegishli malumot bering")
#
# class Author:
#     def __init__(self, name):
#         self.name= name
#
#     def get_info(self):
#         return f"{self.name}"

class Shaxs:
    def __init__(self, name, age, gender, job):
        self.name = name
        self.age = age
        self.gender = gender
        self.job = job

class Talaba(Shaxs):
    def __init__(self, name, age, gender, grades, faculty):
        super().__init__(name, age, gender, job=None)
        self.grades = grades
        self.faculty = faculty

talaba1 = Talaba("Asad", "23", "Erkak", 2, "IT")
print(talaba1)