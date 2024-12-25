# class Student:
#     def __init__(self, name, age, grades):
#         self.name = name
#         self.age = age
#         self.grades = grades
#
#     def get_info(self):
#         print(f"Talabaning ismi {self.name},yoshi {self.age}, bahosi {self.grades}")
#
# student1 = Student("Giyos", 25, "5")
# student2 = Student("Aziz", 28, "5")
# print(student1.age)
# print(student2.age)
# print(student2.get_info())
import pickle

from yangi.hmwk14 import choice


#2
# class User:
#     def __init__(self, name, login, email, age):
#         self.name = name
#         self.login = login
#         self.email = email
#         self.age = age
#
#     def get_info(self):
#         print(f"Foydalanuvchi: ismi ={self.name}, logini {self.login}, emaili {self.email} va yoshi {self.age}")
#
# user1= User("Aziz", "aziziy", "aziziy@gmail.com", 30)
# user2= User("Vaxob", "Vodiyli", "Vax0b@mail.ru,", 23)
#
# user1.get_info()
# user2.get_info()

#3
class LibraryItem:
    def __init__(self,name,upc, subject):
        self.name = name
        self.upc = upc
        self.subject = subject


class Magazine:
    def __init__(self, volume, issue):
        self.volume = volume
        self.issue = issue

class DVD:
    def __init__(self, Actors, Director, Genre):
        self.actors = Actors
        self.director = Director
        self.genre = Genre

class CD:
    def __init__(self, artist):
        self.artist = artist
        

class Book:
    def __init__(self, ISBN, name, subject, dds_number, authors=[]):
        self.ISBN= ISBN
        self.name= name
        self.subject= subject
        self.dds_number= dds_number
        self.authors= authors
    def get_info(self):
        return f"{self.name, self.subject}"

    def get_name(self):
        return self.name

    def get_subject(self):
        return self.subject

    def get_dds_number(self):
        return self.dds_number

    def get_authors(self):
        return self.authors

class Catalog:
    def __init__(self, name):
        self.name = name
        self.books = []

    def search(self, name="", author=""):
        if name:
            book = []
            for i in self.books:
                if i.name == name:
                    book.append(i)
            if book:
                for i in book:
                    print(f"bu kitob {i.dds_number} da joylashgan")
            else:
                print("topilmadi")
        elif author:
            book = []
            for i in self.books:
                if i.author == author:
                    book.append(i)
            if book:
                for i in book:
                    print(f"bu kitob {i.dds_number} da joylashgan")
            else:
                print("author topilmadi")


    def add_book(self,book: Book):
        if isinstance(book, Book):
            self.books.append(book)
            print(f"sizning {book.get_info()} qoshildi")
        else:
            print("siz Book classiga tegishli malumot bering")

class Author:
    def __init__(self, name):
        self.name= name

    def get_info(self):
        return f"{self.name}"

def read_file():
    catalog1 = None
    try:
        with open("Library.dat", "rb") as fayl:
            catalog1 = pickle.load(fayl)
    except Exception as e:
            print(catalog1)
    return catalog1

def write_file(catalog1, *args):
    with open("Library.dat", "wb") as fayl:
        if not catalog1:
            catalog1 = Catalog("Yangi Kutubxona")
        for i in  args:
            if isinstance(i, LibraryItem):
                catalog1.add_book('book')
        pickle.dump(catalog1, fayl)

def main():
    while True:
        print("""
        1. Catalog malumotlarini korish
        2. Item qoshish
        3. chiqish
        """)
        catalog = read_file()
        choices = int(input("menyuni tanlang"))
        if choices == 1:
            print(catalog)
        elif choices ==2:
            cd_list = []
            while True:
                title = input("CD ni titleni kiriting")
                author = input("avtorni kiriting")
                cd_list.append(CD(title, author))
                choice = input("davom etamizmi")
                if choice == "yoq":
                    break
            print(cd_list)
            write_file(catalog, cd_list)
        else:
            break

if __name__ == main():
    main()


# book1 = Book("12221", "Qora", "OQ", "11111", "Willyam")



# catalog1 = Catalog("1-javon")

# try:
#     with open("Library.dat", "rb") as fayl:
#         catalog1 = pickle.load(fayl)
#         print(catalog1)
# except Exception as e:
#     print("exept", e)
#
# with open("Library.dat", "wb") as fayl:
#     book = Book("12221", "Qora", "OQ", "11111", "Willyam")
#     if not catalog1:
#         catalog1 = Catalog("Yangi Kutubxona")
#     catalog1.add_book(book)
#     pickle.dump(catalog1, fayl)





# author1 = Author("Azim Toraev")
# author2 = Author("Mirqosim Juraev")
# book1 = Book(121221, "ona tili 5", "darslik", "1231", [author1])
# book2 = Book(121223221, "rus tili 5", "darslik", "3231", [author2])
# catalog1.add_book(book1)
# catalog1.add_book(book2)
# # catalog1.search("Azim Toraev")
# # authors = Author("")


# print(book2.get_name())
# print(dir(Book))

# for i in dir(Book):
#     if not i.startswith("__"):
#         print(i)