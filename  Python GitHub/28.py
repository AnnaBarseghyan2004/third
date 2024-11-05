x = [12,13,14,14,12,1,20,19,19]
x1=[]

maximum = max(x)
minimum = min(x)

for number in x:
    if x.count(number)==1:
        x1.append(number)
    else:
        x1.append(minimum)
        x1.append(maximum)
print(x1)
        