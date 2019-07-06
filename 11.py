

#9 * 9
i = 1
#j = 1
sum = 1
while i < 10:
    j = 1
    while j <= i:
        sum = i * j
        print("{} * {} = {:2d}".format(j,i,sum),end='  ')
        j = j+1
    i = i+1
    print()

