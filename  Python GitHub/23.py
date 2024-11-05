n = int(input())

arr=[]

for num in range(n):
    arr.append(int(input()))

for i in range(len(arr)):
    if arr[i]==0 and arr[i+1]==0:
        print("array contains consecutive zeroes")
        break
else:
    print("Array does not contain consecutive zeros")

