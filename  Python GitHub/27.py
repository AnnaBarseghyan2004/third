arr = []

for x in range(5):
    arr.append(int(input()))

new_arr = []

for num in arr:
    if 10 <= num <= 99 :
       for i in range(2, int(num**0.5) + 1):
          if num % i == 0:
            break
       else:
          new_arr.append(num)
       
print(new_arr)