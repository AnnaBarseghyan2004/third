print('Enter 5 numbers.')

arr = []

for x in range(5):
    arr.append(int(input()))

result = []

for num in arr:
    result.append(num)
    if num == 9:
        result.append(0)

print(result)
