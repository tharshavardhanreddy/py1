from array import *

a = int(input("enter length of an array"))

arr = array('i', [])

for i in range(a):
    b = int(input("enter value of an array position"))
    arr.append(b)

print(arr)
