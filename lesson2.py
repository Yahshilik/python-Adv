b = "Hello World!"
print(b[6:])
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