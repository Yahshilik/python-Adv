

# def reverse_a(n):
#
#     if n==0:
#         return 0
#     else:
#         return n+reverse_a(n-1)
#
# print(reverse_a(9))

# def kupayt(n):
#     if n==1:
#         return 1
#     return n*kupayt(n-1)
# print(kupayt(5))
menu = {
    "osh": 25000,
    "manti": 15000,
    "shashlik": 10000
}
zakazla = {}

def display():
    for k, v in menu.items():
        print(f"{k}: {v} som")
def zakaz():
    global menu
    while True:
        ovqat = input("Qaysi ovqatni zakaz kilasiz")
        if ovqat in menu.keys():
            zakazla[ovqat]=menu.get(ovqat)
        else:
            print("bunaqa ovqat yoq")
        c = input("Davom etamizmi?")
        if c == "yoq":
            break

def total():
    print(sum(zakazla.values()))
    return sum(zakazla.values())

def discount():
    summ = total()
    prom= input("aksiyadan foydalanmoqchi busayiz promoni kiriting>>")
    if prom == "uz24":
        summ *=0.7
        print("tabriklaymiz", summ)
    else:
        print("kechrass")

def main1():
    choices = ["menyu", "zakaz", "summa", "skidka"]
    while True:
        for index, value in enumerate(choices):
            print(f"{index+1}, {value}")
        choice = int(input("Tartib raqamni tanlang"))
        if choice==1:
            display()
        elif choice==2:
            zakaz()
        elif choice==3:
            total()
        elif choice==4:
            discount()
        else:
            print("Raxmat")
            break

main1()

