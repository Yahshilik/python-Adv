# uz_to_eng = {
#     "salom": "hello",
#     "kitob": "book",
#     "maktab": "school"
# }
#
# eng_to_uz = {
#     "hello": "salom",
#     "book": "kitob",
#     "school": "maktab"
# }
# #So'z qidirish (O'zbekcha-Inglizcha)
# word = input("O'zbekcha so‘zni kiriting: ")
# print(uz_to_eng [word])
#
# #
# uz_to_eng.update({"hayr": "good bye"})
# print(uz_to_eng)
#
# #
# word_to_del = input("O'chirmoqchi bo'lgan O'zbekcha so'zni kiriting: ")
# del uz_to_eng[word_to_del]
# print(uz_to_eng)
#
# ## Dictionarydagi barcha so'zlarni ko'rish (O'zbekcha-Inglizcha) (inglizcha-ozbekchada) for orqali
#
# lugat = [uz_to_eng, eng_to_uz]
# for i in lugat:
#     print(i)

#
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#
tropical = {"pineapple", "mango", "papaya", "apple"}

thisset.update(tropical)

print(thisset)

#
thisset.remove("banana")

print(thisset)

#
x = thisset.pop()

print(x)

print(thisset)

#
for x in thisset:
    print(print(x))

#
print(len(thisset))