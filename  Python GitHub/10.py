numbers = [121, 222, 2, 3, 4, 44544, 535, 51, 511]

def is_symmetric(num):
    num_str = str(num)
    return num_str == num_str[::-1]

def symmetric_list(nums):
    symmetric_numbers = []  
    for i in nums:
        if is_symmetric(i):
            symmetric_numbers.append(i)
    return symmetric_numbers

print(symmetric_list(numbers))
