n = int(input())

arr=[]

for num in range(n):
    arr.append(int(input()))

count1= 0
count2 = 0
gumar = 0
mijintv = 0

for num in arr:
    if num % 3 == 0 :
        count1 += 1
print(count1)

for num in arr:
    if num % 2 == 0:
        gumar += num
        count2 += 1

mijintv = int(gumar / count2 )

print (mijintv)

arr.insert(0,count1)
arr.append(mijintv)

print(arr)


