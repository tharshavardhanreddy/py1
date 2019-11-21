num = int(input("enter value"))

for i in range(2, num):
    if num % i == 0:
        print("not prime")
        break
else:
    print("prime")