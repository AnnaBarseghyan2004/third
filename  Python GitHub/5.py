a = [1,2,4,5]
b = [4,5,8]
c = [2,3,6,8]

set1 = set(a)
set2 = set(b)
set3 = set (c)

common_elem = set1.intersection(set2,set3)

if common_elem:
    print ("their common elems are:" , common_elem)
else:
    print("they have no common elems")