# user_dict = {
#     "admin" : "123",
#     "admin1" : "12",
#     "user1" : "444"
# }
#
# name1 = input("login kiriting>> ")
# passw = input("parol kiriting")
#
# uruniw = 0
#
# while uruniw <3:
#     if name1 in user_dict.keys():
#         if user_dict[name1] == passw:
#             print("siz tizimga kirdingiz")
#             break
#     name1 = input("login kiriting>> ")
#     passw = input("parol kiriting")
#     uruniw +=1
# else:
#     print("3 marta urundingiz va kirolmadingiz")


# 1

# a=20
# b=5
#
# while a > b:
#     a-=b
#     if a == b:
#         print("0 ga teng")
# print(a)

# 2
# a=20
# b=7
# summa = 0
# while a>b:
#     a-=b
#     summa+=1
#     if a<=b:
#         print(summa)

# 3
# n=22
# k=7
# summa=0
# qoldiq=0
# while n>=k:
#      n-=k
#      summa+=1
#      if n<=k:
#          k-=n
#          qoldiq+=n
#          print(qoldiq, "qoldigi")
# print(summa, "butun son")

# 4
# n = 14
#
# while n>=3:
#     n-=3
# if n ==0:
#         print("3 ga karrali")
# else:
#     print("3ga karralimas")
#

# 5


#6
# n= int(input("son kiriting"))
# k= 1
# a = ""
# while n>0:
#     k*=n
#     a += f"*-{n-2}"
#     n-=2
#
# print(k,a)


#7
# n= int(input("son kiriting"))
# k=1
# while n>k*k:
#     k+=1
# print(k)


#8

#9

#10
# n = 50
# k = 1
# while n >=3**k:
#     k+=1
#     if k>n:
#         k-=1
# print(k)


 #11
# n = 18
# summa = 0
# k = 0
#
# while n>=summa:
#     k+=1
#     summa+=k
#     if summa>n:
#         k-=1
# print(k)

#12

#13


#14
# a = int(input("son kiriting"))
# k = 1
# summa = 0
# while summa<=a:
#     if summa>=a:
#         break
#     summa+= 1/k
#     k+=1
# print(k, summa)



#15
# s= 200
# p=8
# oy=0
# summa=0
# while summa<=s:
#     summa+=(s/100)*p
#     oy+=1
#     if summa>=s:
#         break
# print(summa*2, oy)

#15 darsdagisi
# oy=1
# s = int(input("boshlangich summani kiriting"))
# p = int(input("foiz stavka"))
# summa = s
# while summa
#16
# yuguriw = 10
# p = 30
# kun = 0
# masofa = 200
# masofa1 = 0
# while masofa>=yuguriw:
#     kun+=1
#     masofa1+=yuguriw+(yuguriw/100)*p
#     p+=1
#     if masofa<=masofa1:
#         break
# print(kun, masofa1)

eng_to_uz = {
    "hello": "salom",
    "book": "kitob",
    "school": "maktab",
    "house": "uy",
    "friend": "do'st",
    "father": "ota",
    "mother": "ona",
    "city": "shahar",
    "year": "yil",
    "month": "oy",
    "table": "stol",
    "teacher": "o'qituvchi",
    "children": "bolalar",
    "fish": "baliq",
    "meat": "go'sht",
    "green": "yashil",
    "red": "qizil",
    "apple": "olma",
    "bread": "non",
    "water": "suv"
}

uz_to_eng = {
    "salom": "hello",
    "kitob": "book",
    "maktab": "school",
    "uy": "house",
    "do'st": "friend",
    "ota": "father",
    "ona": "mother",
    "shahar": "city",
    "yil": "year",
    "oy": "month",
    "stol": "table",
    "o'qituvchi": "teacher",
    "bolalar": "children",
    "baliq": "fish",
    "go'sht": "meat",
    "yashil": "green",
    "qizil": "red",
    "olma": "apple",
    "non": "bread",
    "suv": "water"
}

#2
word = input("Tarjima uchun so\'z kiriting: ")
if not uz_to_eng.get(word):
    print(f"{word} so\'z hali lug\'atda yo\'q!")
else:
    print(f"{word} ingliz tilida: {uz_to_eng[word]}")

word = input("Enter a word in English: ")
if not eng_to_uz.get(word):
    print(f"{word} in dictionary doesn't exists!")
else:
    print(f"{word} in uzbek: {eng_to_uz[word]}")

#3
word1 = input("Enter an English word to add into English-Uzbek dictionary: ")
word2 = input(f"Enter it is {word1} translation in Uzbek to add into English-Uzbek dictionary: ")
eng_to_uz[word1] = word2
print(f"New word {word1}-{word2} added!")

word1 = input("O\'zbekcha so\'z kiriting: ")
word2 = input(f"Uning {word1} tarjimasini kiriting: ")
uz_to_eng[word1] = word2
print(f"Yangi so\'z {word1}-{word2} qo\'shildi!")

#4
word1 = input("Enter an English word to update a word in English-Uzbek dictionary: ")
if word1 in eng_to_uz:
    word2 = input(f"Enter it is {word1} translation in Uzbek to update a word in English-Uzbek dictionary: ")
    eng_to_uz[word1] = word2
    print(f"Word: {word1}-{word2} updated successfully!!")
else:
    print(f"{word1} doesn\'t exists in English-Uzbek dictionary!")
word1 = input("O\'zbek-Ingliz lug\'atida so\'z yangilash uchun o\'zbekcha so\'z kiriting: ")
if word1 in uz_to_eng:
    word2 = input(f"Uning {word1} tarjimasini kiriting: ")
    uz_to_eng[word1] = word2
    print(f"So\'z {word1}-{word2} yangilandi!")
else:
    print(f"{word1} O\'zbek ingliz lug\'atida yo\'q!")

#5
word_to_delete = input("O'chirmoqchi bo'lgan O'zbekcha so'zni kiriting: ")
if word_to_delete in uz_to_eng:
    del uz_to_eng[word_to_delete]
    print(f"{word_to_delete} muvafaqqiyatli o\'chirildi")
else:
    print(f"{word_to_delete} O\'zbek ingliz lug\'atida yo\'q!")

#6
print(f"English\t Uzbek")
for key, value in eng_to_uz.items():
    print(f"{key}\t {value}")

print(f"\nUzbek\t English")
for key, value in uz_to_eng.items():
    print(f"{key}\t {value}")
print()
