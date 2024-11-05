n = int(input())

arr=[]

for num in range(n):
    arr.append(int(input()))

for i in range(2,len(arr)):
    if arr[i]==0:
        x = arr[i-1] + arr[i-2]
        arr[i]=x
print (arr)
        
        