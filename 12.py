
#
a, b = 0,1
while b<100:
    print("@:a = {},b = {}".format(a,b))
    #a,b = b,a+b
    b,a = a+b,b
    print("#:a = {},b = {}".format(a,b))


