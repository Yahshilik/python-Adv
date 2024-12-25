from abc import ABC, abstractmethod


class Author:
    def __init__(self, name):
        self.name = name

    def get_author_name(self):
        pass

    def set_author_name(self):
        pass

class LibraryItem(ABC):
    __item = 0

    def __init__(self, title, upc, subject):
        self.title = title
        self.upc = upc
        self.subject = subject
        LibraryItem.__item +=1

    @classmethod
    def get_items(cls):
        return cls.__item

    @abstractmethod
    def locate(self):
        pass

    @abstractmethod
    def get_info(self):
        pass

class Book(LibraryItem):
    def __init__(self,title, upc, subject,isbn, dds_number):
        super().__init__(title, upc, subject,)
        self.__isbn = isbn
        self.dds_number = dds_number
        self.authors = []

    def get_authors(self, author):
        pass

    def locate(self):
        return self.dds_number

    def get_info(self):
        return f"{self.title}"

class DVD(LibraryItem):
    def __init__(self, title, janr):
        super().__init__(title, upc=None, subject=None)
        self.janr = janr

    def locate(self):
        return self.janr + " " +self.title

    def get_info(self):
        return f"{self.title}"

class Catalog:
    def __init__(self):
        self.items = []

    def add_item(self, item: Book | DVD):
        self.items.append(item)

    def search(self, keyword):
        item = []
        # if keyword in self.items:
        for i in self.items:
            if i in self.items:
                item.append(i.locate())

        return item

book1 = Book("asas", "asssa", "qaaa", "12121", "45451")
dvd = DVD("sasaa", "sssa")

# print(book1.locate())
catalog = Catalog()
catalog.add_item(book1)
catalog.add_item(dvd)

print([i for i in catalog.search("asas")])