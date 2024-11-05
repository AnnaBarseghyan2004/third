numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5]
not_same = []

def funtion_1(num):
    for i in num:
        if num.count(i) == 1:
            not_same.append(i)  
    return(not_same)

   
  
print(funtion_1(numbers))



