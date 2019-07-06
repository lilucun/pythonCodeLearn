
#!/usr/bin/env python3
N = 10
sum = 0
count = 0
print("please input 10 nums:")
while count < N:
    number = float(input())
    sum += number
    count += 1
ave = sum / 10
print("N = {},sum = {}".format(N,sum))
print("ave = {:.3f}".format(ave))
