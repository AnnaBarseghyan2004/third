array = []

for i in range(4):
    array.append(int(input()))

def is_palindrome(array):
    reversed_array = array[::-1]
    return array == reversed_array

if is_palindrome(array):
    print('Array is a palindrome')
else:
    print('Array is not a palindrome')


    