from array import *

a = int(input("enter length of an array"))

arr = array('i', [])

for i in range(a):
    b = int(input("enter value of an array position"))
    arr.append(b)

print(arr)

c = int(input("enter number to know index"))
e = 0
for d in arr:
    if d == c:
        print(e)
        break
    e += 1

print(arr.index(c))

for f in arr:
    if f >= c:
        print(f, "greater", c)
    else:
        print(f, "small", c)

else:
    print("equal")