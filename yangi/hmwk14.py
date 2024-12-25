# menyu = {}
restoran = True


class Ovqat:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def new_price(self, yangi_narx):
        self.price = yangi_narx

    def get_name(self, name):
        return self.name

    def get_price(self, price):
        return self.price

    def get_info(self):
        return f"{self.name} -  {self.price} som"


class Menyu:
    def __init__(self):
        self.ovqatlar = []

    # def menyu_add(**kwargs):
    #     global menyu
    #     for i, j in kwargs.items():
    #         menyu[i] = j


    def ovqat_add(self, ovqat:Ovqat):
        if isinstance(ovqat, Ovqat):
            self.ovqatlar.append(ovqat)
            print(f"Yangi taom qoshildi = {ovqat.get_info()}")
        else:
            print("Malumot notogri kiritilgan")

    def ovqat_delete(self, ovqat:Ovqat):
        for ovqat in self.ovqatlar:
            self.ovqatlar.remove(ovqat)
            print(f"{ovqat} taom ochirildi")
        else:
            print(f"{ovqat} taom topilmadi")

    def narxni_ozgartirish(self, ovqat: Ovqat, yangi_narx):
        if ovqat in self.ovqatlar:
            ovqat.new_price(yangi_narx)
            print(f"Taom narxi yangilandi = {ovqat.get_info()}")
        else:
            print("Malumot notogri kiritilgan")

    def get_ovqatlar(self):
        return self.ovqatlar

    def menyuni_korish(self):
        if not self.ovqatlar:
            print("Hali menuda taomlar qoshilmagan")
        else:
            for ovqat in self.ovqatlar:
                print(ovqat.get_info())


class Promocode:
    def __init__(self, promocode, percentage):
        self.promocode = promocode
        self.percentage = percentage

    def get_promocode(self):
        return self.promocode

    def get_percentage(self):
        return self.percentage

    def promocode_ishlatsh(self, total_price):
        promocode = total_price * (self.percentage / 100)
        return total_price - promocode


promocode1 = Promocode('uz24', 30)
promocode2 = Promocode('uz23', 25)

class Zakazlar:
    def __init__(self, menyu: Menyu):
        self.menyu = menyu
        self.zakazlar = []
        self.total = 0

    def zakaz(self, nomi=""):
        if nomi:
            for i in self.menyu.get_ovqatlar():
                if i.get_name() == nomi:
                    self.zakazlar.append(i)
                    self.total += i.get_price()
                    print(f"Zakazingiz qabul qilindi = {i.get_info()}")
                    return
            print("Unday taom topilmadi")

    def total_narx(self, promocode: Promocode = None):
        if promocode:
            promocodeli_narx = promocode.promocode_ishlatsh(self.total)
            print(f"Promo kod {promocode.get_promocode()} qo'llanildi. Chegirmali total: {promocodeli_narx} so'm.")
        else:
            print(f"Total chek - {self.total} so'm.")


menyu = Menyu()
zakazlar = Zakazlar(menyu)

# menyu_add(**{"osh": 25000, "manti": 15000, "lagmon": 20000, "shashlik": 10000})
# menyu_add(**{"salat": 8000, "choy": 4000})

while True:
    print(f"""
           MAIN MENU:

    1. Ovqatlar bilan ishlash
    2. Ovqatlar menusini korish
    3. Zakaz qilish
    4. Promocode ishlatsh
    5. Total summani korish
    6. Restorandan chiqish
    """)

    try:
        choice = int(input("Tanlovingizni kiriting: "))
        if choice < 1 or choice > 6:
            raise ValueError
        else:
            match choice:
                case 1:
                    print(f"""
    Ovqatlar bilan ishash:

    1. Menyuga yangi taom qoshish
    2. Menyudagi taomni ochirish
    3. Taomni narxini ozgartirish
    4. Bosh menuga chiqish
                    """)
                    try:
                        choice = int(input("Tanlovingizni kiriting: "))
                        if choice < 1 or choice > 4:
                            raise ValueError
                        else:
                            match choice:
                                case 1:
                                    yangi_taom = input("Yangi taom/ichimlik/salat nomini kiriting: ")
                                    yangi_taom_narxi = float(input("Yangi taom narxini kiriting: "))
                                    ovqat = Ovqat(yangi_taom, yangi_taom_narxi)
                                    menyu.ovqat_add(ovqat)
                                case 2:
                                    ochiriladigan_taom = input("Ochirmoqchi bolgan taomingizni nomini kiriting: ")
                                    for ovqat in menyu.get_ovqatlar():
                                        if ovqat.get_name() == ochiriladigan_taom:
                                            menyu.ovqat_delete(ovqat)
                                            break
                                    else:
                                        print("Bunday taom menudan topilmadi")
                                case 3:
                                    ozgariladigan_taom = input("Narxini ozgartirmoqchi bolgan taomni nomini kiriting: ")
                                    yangi_narx = float(input("Yangi narxini kiriting: "))
                                    for taom in menyu.get_ovqatlar():
                                        if taom.get_name() == ozgariladigan_taom:
                                            menyu.narxni_ozgartirish(taom, yangi_narx)
                                            break
                                    else:
                                        print("Bunday taom menudan topilmadi")
                                case 4:
                                    continue
                    except ValueError:
                        print("Faqat 1 va 4 orasini tanlang")
                case 2:
                    print("Taomlar Menusi:")
                    menyu.menyuni_korish()
                case 3:
                    print("Menuni korib, bor taomlardan tanlang:")
                    menyu.menyuni_korish()
                    zakaz = input("Taom nomini kiriting: ")
                    zakazlar.zakaz(nomi="")
                case 4:
                    promocode = input("Promocodni kiriting: ")
                    if promocode == promocode1.get_promocode():
                        zakazlar.total_narx(promocode1)
                    elif promocode == promocode2.get_promocode():
                        zakazlar.total_narx(promocode2)
                    else:
                        print("Notogri promocode")
                case 5:
                    print("Total check:")
                    zakazlar.total_narx()
                case 6:
                    print("Sizni yana kutamiz!")
                    break
    except ValueError:
        print("Boshqattan harakat qilib koring")
# print(ovqat3.get_info())



