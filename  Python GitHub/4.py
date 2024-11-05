a = [1,2,3,4,5]
b = [6,2,8,9,10]

for elem1 in a:
    for elem2 in b:
        if elem1 == elem2 :
            print ("they have at least one common element.")
            break
