# name = "o\\lam"
# print(name)
#
# kocha = input("kochangizni kiriting>>")
# mahalla = input("mahallangizni kiriting>>")  # ctrl+d kopiyalash
# tuman = input("tumaningizni kiriting>>")
#
# print(f"{kocha} kochasi,\n {mahalla} mahallasi,\n {tuman} tumani")
# manzil = f"{kocha} kochasi,\n {mahalla} mahallasi,\n {tuman} tumani"
# print(manzil)
# manzil = manzil.lower()
# print(manzil)
# manzil = manzil.capitalize()
# print(manzil)
# manzil = manzil.upper()
# print(manzil)
# manzil = manzil.title()
# print(manzil)
from itertools import filterfalse

# boolean
# son=int(input("butun son kirit>>")) #juft sonlarni tasdiqlash
# toq_son=son%2==0
# print(toq_son)
# son=int(input("butun son kirit>>")) #manfiy son tasdiqlash
# mson = son<0
# print(mson)

#
xson = int(input("x son kirit"))
yson = int(input("y son kirit"))
a = xson + yson
j = a % 2 == 0
print(j)
print(not (j))
