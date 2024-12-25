from itertools import product

# product = {}
# def prodict_add(**kwargs):
#     pass
#
# def product_info():
#     pass
#
#
# def main():
#     choices = ["mahsulot qushish", "mahsulot ochirish", "maxsulon malumotlarni korish", "maxsulotni ozgartirish", "Exit"]
#     for index, value in enumerate(choices):
#         print((f"{index + 1}.{value}"))



# def summa(*args, **kwargs):
#     result = 0
#     print(args)
#     print(kwargs)
#     for i in args:
#         result +=1
#
#     for v in kwargs.values():
#         result +=v
#     return result
#
# summa (1, 2,3,4,5, **{"a":12, "b":9})


# result = 1
#
# def change_global():
#     global result
#     result = 13
#     print(result)
#
# change_global()
# print(result)


product = {}


def product_add(**kwargs):
    global product

    for name, amount in kwargs.items():
        if name in product.keys():
            product[name] += amount
            print(f"{name} mahsuloti {product[name]}ga ozgartirildi")
        else:
            product[name] = amount
            print((f"{name} mahsoloti {amount}ta keltirildi"))


def product_delete(*args):
    global product
    for i in args:
        if i in product:
            del product[1]
            print(f"{i} mahsulotiochirildi")
        else:
            print(f"{i}mahsuloti skladda yuq")



def product_info(*args):
    if args:
        for i in args:
            if i in product:
                print(f"{i} mahsulotidan skladda {product[i]} ta bor")
            else:
                print('siz soragan mahsulot yoq')
    else:
        for k,v in product.items():
            print(f"{k}dan, {v}ta bor")

def product_update(name, amount):
    global product
    if name in product:
        product[name] +=amount
        print(f"{name} mahsuloti {amount}ta keltirildi")
    else:
        product[name] = amount
        print((f"{name} mahsuloti {amount} ta keltirildi"))


def product_amount(*args):
    pass


product_add(**{"olma": 4, "anor": 9})
product_add(**{"anjir": 5})
# product_update("anor",8)
# product_info()


def main():
    choices = ["mahsulot qoshish","mahsulot ochirish","mahsulot malumotlarini korish", "mahsulotni ozgartirish", "exit"]
    for index, value in enumerate(choices):
        print(f"{index+1}, {value}")
    while True:
        choice = int(input("Tartib raqamini tanlang, qaysi funksiyadan foydalanmoqchisiz"))
        if choice==1:
            m = {}
            while True:
                client = input("mahsulot kiritasizmi? (ha, yoq)")
                if client.lower() == "ha":
                    product1 = input("mahsulotni kiriting>>")
                    amount1 = int(input("miqdorini kiriting>>"))
                    m[product1]=amount1
                else:
                    product_add(**m)
                    break

        elif choice==2:
            while True:
                client = input("mahsulot ochirasizmi? (ha, yoq)")
                if client.lower() == "ha":
                    product1 = input("mahsulotni kiriting>>")
                    product_delete(product1)

                else:
                    break

        elif choice == 3:
            while True:
                client = input("xamma mahsulotni kormoqchimisiz? yoki bitta mahsulotnimi(xamma, bitta, yoq)")
                if client.lower() == "xamma":
                    product_info()
                elif client.lower() == "bitta":
                    product1 = input("mahsulotni kiriting>>")
                    product_info(product1)
                else:
                    break

        elif choice==4:
            m = {}
            while True:
                client = input("mahsulot ozgartirasizmi? (ha, yoq)")
                if client.lower() == "ha":
                    product1 = input("mahsulotni kiriting>>")
                    amount1 = int(input("miqdorini kiriting>>"))
                    m[product1] = amount1
                else:
                    product_add(**m)
                break

        else:
            break

main()