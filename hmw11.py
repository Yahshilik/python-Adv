books = {}


def book_add(**kwargs):
    global books
    print(kwargs)
    for name, amount in kwargs.items():
        if name in books.keys():
            books[name] += amount
            print(f"{name} kitobi {books[name]}ga ozgartirildi")
        else:
            books[name] = amount
            print((f"{name} kitobi {amount}ta keltirildi"))


def book_del(*args):
    global books
    for i in args:
        if i in books:
            del books[i]
            print(f"{i} kitobi ochirildi")
        else:
            print(f"{i}kitobi xisobda yuq")


def book_info(*args):
    if args:
        for i in args:
            if i in books:
                print(f'{i} kitobi xisobda {books[i]}ta bor')
            else:
                print("siz soragan kitob yoq")
    else:
        for k, v in books.items():
            print(f"{k}dan, {v}ta bor")


def book_up(name="", amount=""):
    global books
    if name in books:
        books[name] += amount
        print(f"{name} kitobi {amount} ta keltirildi")
    else:
        books[name] = amount
        print((f"{name} mahsuloti {amount} ta keltirildi"))


book_add(**{"lugat": 3, "atlas": 5, "darslik": 10})
# book_up(**{"badiy": 15})


def main():
    choices = ["kitob qoshish", "kitob ochirish", "kitoblar xaqida korish", "kitoblarni ozgartirish", "exit"]
    for index, value in enumerate(choices):
        print(f"{index + 1}, {value}")
    while True:
        while True:  # 1
            choice = int(input("Tartib raqamini tanlang, qaysi funksiyadan foydalanmoqchisiz"))
            if choice == 1:
                m = {}
                while True:
                    client = input("kitob kiritasizmi? xa, yoq>>")
                    if client.lower() == "xa":
                        book1 = input("kitobni kiriting>")
                        amount1 = int(input("nechta?"))
                        m[book1] = amount1
                    else:
                        book_add(**m)
                        break

            elif choice == 2:
                while True:
                    client = input("kitobni ochirasizmi? (xa, yoq)")
                    if client.lower() == "xa":
                        book1 = input("kitobni kiriting>>")
                        book_del(book1)
                        yana = input("Yana kitob ochirasizmi? (ha, yoq): ")
                        if yana == "ha" or yana == "HA":
                            continue
                    else:
                        break

            elif choice == 3:
                while True:
                    client = input("barcha kitoblarni kormoqchimisiz? yoki bittasini(barcha, bitta, yoq)")
                    if client.lower() == "barcha":
                        book_info()
                    elif client.lower() == "bitta":
                        book1 = input("kitobni kiriting>>")
                        book_info(book1)
                    else:
                        break
            elif choice == 4:
                print("\nKITOB MALUMOTINI OXGARTIRISH:")
                ozgartirish = True
                while ozgartirish:
                    ozgarishga_kitob = input("Ozgartirmoqchi bolgan kitobingizni nomini kiriting: ")
                    soni = int(input("Qoshiladigan kitoblar sonini kiriting: "))
                    book_up(ozgarishga_kitob, soni)
                    yana = input("Yana kitob malummotini ozgartirasizmi? (ha, yoq): ")
                    if yana == "ha" or yana == "HA":
                        continue
                    else:
                        ozgartirish = False


            else:
                break


main()
