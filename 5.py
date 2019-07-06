

x = 1
n = 10
i = 0
sum = 0
#while i < n:
for i in range(0,11):
    sum += 1.0 / x
    x += 1
    i = i+1
    print("i = {:2d} , sum = {:.4f}".format(i,sum))

