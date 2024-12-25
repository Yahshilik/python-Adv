# komple= {
#     "admin": "123",
#     "admin1": "123",
#     "user": "444",
#     "user1": "555"
# }
#
# xarakat = 0
#
# ism = input("login kiriting>>")
# parol = input("parol kiriting")
#
# while xarakat <3:
#     if ism in komple.keys():
#         if komple[ism]==parol:
#             print("tizimga kirdingiz")
#             break
#     ism = input("login kiriting>>")
#     parol = input("parol kiriting")
#     xarakat +=1
# else:
#     print("tizimga kiraolmadingiz")
import random
a = random.randint(1,10)

client_ans = int(input("1 dan 11 gacha son kiriting"))

while client_ans !=a:
    if client_ans > a:
        client_ans = int(input(f"{client_ans}dan kicik son tanla"))
    elif client_ans < a:
        client_ans = int(input(f"{client_ans}dan katta son tanla"))
else:
    print("topdingiz")

# client_ans = int(input("1 dan 11 gacha son kiriting"))
# while client_ans !=a:
#     if a < client_ans:
#         client_ans = int(input(f"{client_ans}dan kichikro son tanla"))
#     elif a> client_ans:
#         client_ans = int(input(f"{client_ans}dan kattaro son tanla"))
# else:
#     print("topdingiz")

