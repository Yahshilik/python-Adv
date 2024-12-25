import  csv

# with open("data.csv", "w", newline="") as fayl:
#     writer = csv.writer(fayl)
#     writer.writerows(["ism", "yosh", "bosqich"])
#     writer.writerows(["Ali", "22", "1"])

data = [
    {"ism": "Ali", "yoshi": "22", "ingliz_tili": "5", "rus_tili": "5"},
    {"ism": "Vali", "yoshi": "24", "ingliz_tili": "5", "rus_tili": "4"},
    {"ism": "Alisher", "yoshi": "21", "ingliz_tili": "4", "rus_tili": "3"}
]
def write(data):
    with open("data.csv", "w", newline="") as fayl:
        main= ["ism", "yoshi", "ingliz_tili", "rus_tili"]
        w= csv.DictWriter(fayl, fieldnames=main)
        w.writeheader()
        w.writerows(data)

# with open("data.csv", "r") as fayl:
#     reader= csv.reader(fayl)
#     for i in reader:
#         print(i)

# with open("data.csv", "r") as fayl:
#     reader = csv.DictReader(fayl)
#     talaba = 0
#     yoshi = 0
#     for i in reader:
#         talaba +=1
#         yoshi += int(i.get("yoshi", 0))
    # print("ortacha yoshi", yoshi/talaba)

# talaba_dct = {"ism": "Alijon", "yoshi": "25", "ingliz_tili": "3", "rus_tili": "5"}
# data.append(talaba_dct)
# # with open("data.csv", "r") as fayl:
#     reader = csv.DictReader(fayl)
#     talaba = 0
#     yoshi = 0
#     answer = input("ingliz tilidagi baxolarni kurmoqchimisiz?>>xa yoki yoq")
#     if answer.lower() == "xa":
#         for i in reader:
#             print(f"{i.get("ism")} talaba ingliz tilidan {i.get("ingliz_tili")}")

# import json
# filename = "24_hour_forecast.json"
# with open(filename) as fayl:
#     hour = fayl.read()
#     dt = []
#     for i in hour:
#         dt.append(i.get("dt"))
#         print(dt)

