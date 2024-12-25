
menyu1 = {
    "osh" : 25000,
    "manti" : 15000,
    "shashlik" : 10000,
    "salat" : 5000,
    "non" : 2000
}

zakazlarim = {}

def display_menyu():
    for k, v in menyu1.items():
        print(f"{k}:{v} som")

def zakaz_menyu():
    global menyu1
    while True:
        ovqat = input("Qaysi ovqatni zakaz qilasiz?")
        if ovqat in menyu1.keys():
            zakazlarim(ovqat)==menyu1.get(ovqat)
        else:
            print("afsuski bu ovqat yoq")
            c = input("yana zakaz qilasizmi?")
            if c == "yoq":
                break
def summa_menyu():
    print(sum(zakazlarim.values()))
    return sum(zakazlarim.values())

def skidka_menyu():
    summa=summa_menyu()
    prom = input("aksiyadan foydalanmoqchimisiz? Promokodni kiriting>>")
    if prom == "uz24":
        summa *= 0.7
        print("tabriklaymiz, sizga chegirma", summa)
    else:
        print("kechirasiz")



def main():
    choices = ["Menyuni korish", "Zakaz berish", "Xisob", "Promo kiritish"]
    while True:
        for index, value in enumerate(choices):
            print(f"{index+1}.{value}")
        choice = int(input("Tartib raqamini kiriting>>"))
        if choice == 1:
            display_menyu()
        elif choice == 2:
            zakaz_menyu()
        elif choice == 3:
            summa_menyu()
        elif choice == 4:
            skidka_menyu()
        else:
            print("Tanlovingiz uchun Raxmat")
            break

main()
