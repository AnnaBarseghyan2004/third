array = []

for x in range (4):
    array.append(int(input()))

if len(array) > 10 :
    del array[3]
    del array [7]
    print (array)
else :
    print (' length is not more than 10 ')

