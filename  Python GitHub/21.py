n = int(input())

arr=[]

for num in range(n):
    arr.append(int(input()))

i = 0
while i < len(arr):
    if arr[i] >= 15 and arr[i] <= 105:
       arr.remove(arr[i])
    else:
        i += 1
print(arr)

