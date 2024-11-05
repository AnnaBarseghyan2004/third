array = []

for x in range(5):
    array.append(int(input()))

minimum = min(array)

for i in range (len(array)):
    if array[i] == minimum :
        array[i] = '***'

print (array)
    