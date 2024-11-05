import math
x = int(input())
multiply = 1

if 0 < x < 10 :
    print (math.factorial (x))
elif 10 <= x < 100 :
    print (x**2)
elif x <= 0 :
    print ("not valid")
else :
    print ("Big number")