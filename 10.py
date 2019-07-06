

#else if == elif
a = int(input("input a num:"))
if a > 1:
    print("> 1")
    a = 0
elif a == 0:
    print("a==0")
    a = 1
elif a == 1:
    print("a == 1")
    a = -22
else:
    print("< 0")
