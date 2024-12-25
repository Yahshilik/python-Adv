# 1
a = 4
A = a > 0
print("son musbat", A)
# 2
a = 5
A = a % 2 != 0
print("son toq", A)
# 3
a = 7
A = a % 2 == 0
print("son juft", A)
# 4
a = 5
b = 8
A = a > 2
B = b <= 3
print(A)
print(B)
# 5
a = 7
b = 4
A = a >= 0
B = b < -2
print(A)
print(B)

# 6
a = 3
b = 7
c = -1
R = a <= b <= c
print(R, "1")
# 7
a = 1
b = 5
c = 9
R = a < b < c
print(R)
# 8
a = 4
b = 8
T = a % 2 == 1
T1 = b % 2 == 1
Ts = T + T1 == 2
print(Ts)
# 9

# 9
A = int(input("A soni kiriting>>"))
B = int(input("B soni kiriting>>"))

Holat = A % 2 == 1 or B % 2 == 1
print(Holat)
# 10
A = int(input("A soni kiriting>>"))
B = int(input("B soni kiriting>>"))
bitta_toq = (A % 2 == 1 or B % 2 == 0) or (A % 2 == 0 or B % 2 == 1)
print(bitta_toq)
# 11
A = int(input("A soni kiriting>>"))
B = int(input("B soni kiriting>>"))
toqjuft = (A % 2 == 1 and B % 2 == 1) or (A % 2 == 0 and B % 2 == 0)
print(toqjuft)
# 12
a = 2
b = 5
c = -1
musbat = a > 0 and b > 0 and c > 0
print(musbat)
# 13
A = int(input("A soni kiriting>>"))
B = int(input("B soni kiriting>>"))
C = int(input("C soni kiriting>>"))
Holat = A > 0 or B > 0 or C > 0
print(Holat)
# 14
A = int(input("A soni kiriting>>"))
B = int(input("B soni kiriting>>"))
C = int(input("C soni kiriting>>"))
Holat = (A > 0 and B < 0 and C < 0) or (A < 0 and B > 0 and C < 0) or (A < 0 and B < 0 and C > 0)
print(Holat)
# 15
A = int(input("A soni kiriting>>"))
B = int(input("B soni kiriting>>"))
C = int(input("C soni kiriting>>"))
Holat = (A > 0 and B > 0 and C < 0) or (A < 0 and B > 0 and C > 0) or (A > 0 and B < 0 and C > 0)
print(Holat)
# 16
m = 15
x = (9 < m < 100) % 2 == 0
print(x)
# 17
m = 444
x = (99 < m < 1000) % 2 == 1
print(x)
# 18
A = int(input("A soni kiriting>>"))
B = int(input("B soni kiriting>>"))
C = int(input("C soni kiriting>>"))
X = (A == B or B == C or A == C)
print(X)
# 19
A = int(input("A soni kiriting>>"))
B = int(input("B soni kiriting>>"))
C = int(input("C soni kiriting>>"))
X = (A + B == 0 or B + C == 0 or A + C == 0)
print(X)

# 20
a = 345
bir = a % 10
on = (a // 10) % 10
yuz = a // 100
X = bir != on != yuz
print(X)
# 21
a = 369
bir = a % 10
on = (a // 10) % 10
yuz = a // 100
X = bir < on < yuz
print(X)
# 22
a = 535
bir = a % 10
on = (a // 10) % 10
yuz = a // 100
X = (bir < on < yuz) or (bir > on > yuz)
print(X)
# 23
a = 369
bir = a % 10
on = (a // 10) % 10
yuz = a // 100
X = bir == yuz
print(X)
# 24 tugrisi tushunmadim
A = int(input("A soni kiriting(0 dan katta)>>"))
B = int(input("B soni kiriting>>"))
C = int(input("C soni kiriting>>"))
D = (b ** 2) - (4 * a * c)
T = A*x**2+B*x+C == 0
# 25
x = 5
y = 8
K = (x < 0 and y > 0)
print(K)
# 26
x = 5
y = -5
K = (x > 0 and y < 0)
print(K)
# 27
x = -5
y = 8
K = (x < 0 and y > 0) or (x < 0 and y < 0)
print(K)
# 28
x = 9
y = 8
K = (x > 0 and y > 0) or (x < 0 and y < 0)
print(K)
# 29
x = 2
y = 2
x1 = 1
y1 = 4
x2 = 4
y2 = 1
c = (x1 < x < x2) and (y2 < y < y1)
print(c)
# 30
a = 2
b = 5
c = -1
yon = a == b == c
print(yon)
# 31
a = 2
b = 5
c = -1
yon = a == b or b == c or a == c
print(yon)
# 32
a = 2
b = 5
c = -1
yon = a == b or b == c or a == c
print(yon)
# 33
a = 2
b = 3
c = 5
con = a + b > c and b + c > a and c + a > b
# 34
x = 8
y = 5
oq = (x + y) % 2 == 1
# 35
x1 = 8
y1 = 5
x2 = 3
y2 = 2
birxilrang = ((x1 + y1) % 2 == 1 and (x2 + y2) % 2 == 1) or ((x1 + y1) % 2 == 0 and (x2 + y2) % 2 == 0)
print(birxilrang)
# 36
x1 = 4
y1 = 5
x2 = 3
y2 = 1
ruh = abs(x2 - x1) == 1 and abs(y2 - y1) == 1
print(ruh)
# 37
# shox ning yurishi
x1 = 1
y1 = 1
x2 = 2
y2 = 2
gorizontal = abs(x2 - x1) == 1
print(gorizontal)
vertical = abs(y2 - y1) == 1
print(vertical)
diaganal = abs(abs(x1 - x2) == 1 and abs(y2 - y1) == 1)
print(diaganal)
# 38
x1 = 4
y1 = 5
x2 = 3
y2 = 1
fil = abs(abs(x2 - x1) == 1 and abs(y2 - y1 == 1))
print(fil)
