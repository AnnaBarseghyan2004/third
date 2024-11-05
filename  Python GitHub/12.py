print ('Enter 5 numbers.')
arr = []
count = 0

for i in range (5):
    arr.append(int(input())) 

for x in range(5) :
    if arr[x] % 2 == 0:
        count += arr[x]

print (count)

