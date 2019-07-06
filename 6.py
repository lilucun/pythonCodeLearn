

import math
a = int(input("input value of a:"))
b = int(input("input value of b:"))
c = int(input("input value of c:"))
d = b * b - 4 * a *c
if d < 0:
	print("roots are imaginary")
else:
	root1 = (-b + math.sqrt(d))
	root2 = (-b - math.sqrt(d))
	print("root1 = {}".format(root1))
	print("root2 = %d", root2)

