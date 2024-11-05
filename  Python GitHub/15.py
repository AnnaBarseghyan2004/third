array = []

for x in range (10):
    array.append(int(input()))

number_of_elements = len(array)

if len(array) < 10:
    array.clear()
    for i in range(int(number_of_elements)):
        array.append(0)
    print(array)
else:
    print ('Array has more than or equil 10 elements.')
