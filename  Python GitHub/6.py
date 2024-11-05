a = [1,2,3,4,5]
b = [2,8,7,54,2]

missinginb = []
missingina = []

for elem1 in a:
    if elem1 not in b:
        missinginb.append(elem1)

for elem2 in b:
    if elem2 not in a:
        missingina.append(elem2)


print ("missing in b :" , missinginb)
print("missing in a:" , missingina)

            
