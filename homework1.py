print("salom")
#1
a=5
P=a*4
print (P)
#2
S=a**2
print(S)
#3
b=3
s=a*b
P=2*(a+b)
print ("tortburchakning yuzasi:", s)
print ("tortburchakning perimetri:", P)
#4
d=7
pi=3.14
L=pi*d
print ("aylana uzunligi", L)
#5
a=6
V=a**2
S=6*a**2
print ("kubning hajmi:", V)
print ("kubning sirti:", S)
#6
c=2
V=a*b*c
S=2*(a*b+b*c+a*c)
print ("paralepipedning hajmi:", V)
print ("paralepipedning tola sirti:", S)
#7
R=7
L=2*pi*R
S=pi*R**2
print("Doiraning uzunligi:", L)
print("doiraning yuzasi:", S)
#8
A=(a+b)/2
print("a va b ning urta arifmetigi:", A)
#9
G=(a*b)**0.5
print (G)
#10
t=(a+b)
k=(a*b)
kv1=(a**2)
kv2=(b**2)
print("yigindi:",t)
print("kupaytmasi:",k)
print("a kvadrati:", kv1)
print ("b kvadrati:", kv2)
#11
a=4
b=6
t=(a+b)
k=(a*b)
m1=(a+0)
m2=(b+0)
print("yigindi:",t)
print("kupaytmasi:",k)
print("a moduli:", m1)
print ("b moduli:", m2)
#12
c=(a**2+b**2)**0.5
P=a+b+c
print("togri uchburchakning gipotenuzasi:", c)
print("perimetri:", P)
#13
R1=7
R2=8
S1=pi*R1
S2=pi*R2
S3=pi*(R2-R1)
print("S1ning yuzasi:", S1)
print("S1ning yuzasi:", S2)
print("S1ning yuzasi:", S3)
#14
L=14
R=L/(2*pi)
S=pi*(R**2)
print("aylananing radiusi:", R)
print("aylananing yuzi:",S)
#15
S=20
R=(S/pi)**0.5
D=R*2
print("aylananing diametri:",D)
print("aylananing radiusi:", R)

#16
x1=8
x2=14
M=(x2-x1)
print("2 nuqta orasidagi masofa:", M, "ga teng")
#17
A = 4
B = -3
C = 6
AC = C - A
BC = C - B
L = BC + AC
print("AC ning uzunligi:", AC)
print("BC ning uzunligi:", BC)
print("ikkala kesma yigindisi:", L)
#18
A = 2
B = 9
C = 6
AC = C - A
BC = B - C
K = BC * AC
print("AC ning uzunligi:", AC)
print("BC ning uzunligi:", BC)
print("ikkala kesma kopaytmasi:", K)

#19
x1, y1, = int(input("x1 nuqta:")), int(input("y1 nuqta:"))
x2, y2, = int(input("x2 nuqta:")), int(input("y2 nuqta:"))
a = x2 - x1
b = y2 - y1
p = 2 * (a + b)
s = a * b
print("P:", p)
print("S:", s)
#20
x1=3
x2=7
y1=4
y2=5
m=((x2-x1)**2+(y2-y1)**2)**0.5
print ("masofa:", m, "Ga teng")
# 21
x1 = 3
y1 = 2
x2 = 5
y2 = 6
x3 = 4
y3 = -2
a = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)
b = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** (1 / 2)
c = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** (1 / 2)
p = (a + b + c) / 2
S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(p, S)

#22
a = 5
b = 10
temp = a
a = b
b = temp
print("a:", a)
print("b:", b)
#23
a = 4
b = 8
c = 2
temp = a
a = b
b = temp
temp = b
b = c
c = temp
temp = c
c = a
a = temp
print("a", a)
print("b", b)
print("c", c)

