array = [1, 2, 3, 4, 5, 4, 3]
array_with_not_repetitive_elements = []

for num in array:
    if num not in array_with_not_repetitive_elements:
        array_with_not_repetitive_elements.append(num)

print(array_with_not_repetitive_elements)