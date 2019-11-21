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
