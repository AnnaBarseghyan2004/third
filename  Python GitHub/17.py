array = []

for x in range(5):
    array.append(int(input()))

maximum = max(array)

for i in range (len(array)):
    if array[i] == maximum :
        array[i] = '***'

print (array)
    