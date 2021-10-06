import random
n = 10
a = [0 for i in range(0, n)] #tạo số lượng phần tử của mảng
for i in range(0, n):
    #a[i] = random.randrange(0, 10)
    a[i] = int(input("a["+ str(i)+ "]="))

for i in range(0, n):
    print(a[i], end="  ")
    
print()

def sumEven(a):
    sumeven = 0
    for i in range(0, n):
        if a[i]%2 == 0:
            sumeven+=a[i]
    print("SumEven = ", sumeven)
    
def sumOdd(a):
    sumodd = 0
    for i in range(0, n):
        if a[i]%2 != 0:
            sumodd+=a[i]
    print("SumOdd = ", sumodd)
def sum(a):
    sum1 = 0
    for i in range(0, n):
        sum1+=a[i]
    print("Sum = ", sum1)

sumEven(a)
sumOdd(a)
sum(a)