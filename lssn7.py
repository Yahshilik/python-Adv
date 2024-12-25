# 1-100
bir_yuz = range(1, 100)
print(bir_yuz)
for i in bir_yuz:  # i uzgaruvchi
    print(i)


k = int(input("nechi karra kerak>>"))
# ketma_ket = range(1,10)
for i in range(1, 10):  # i=1,2,3,4,5,6,7,8,9
    print(f"{k}x{i}={k * i}")  # k=3 i=1 3x1=3
else:
    print("tugadi")
# break
k = int(input("nechi karra kerak>>"))
for i in range(1, 10):
    if i == 9:
        break
        print(f"{k}x{i}={k * i}")
else:
    print("break")

# 5bozorlik

n = int(input("nechta mahsulot olasiz"))
bozorlik = []
for i in range(n):
    bozorlik.append(input("nima olmoqchisiz"))
    print(bozorlik)

# Hello
for i in "Hello":
    if i.isupper():
        print(i)




# karra jadval
for i in range(1,10):
    for j in range(1,10):
        if j==1 and i!=1:
            print(f"{i}*{j}={i * j}")
        else:
            print(f"{i}*{j}={i * j}", end='\t')