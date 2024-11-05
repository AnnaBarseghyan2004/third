str1 = "a b c d e f"
str2 = "g h a i j k"

list1 = str1.split()
list2 = str2.split()

both_str1_and_str2_have = []

for char in list1[:]:  
    if char in list2:
        list1.remove(char)  
        both_str1_and_str2_have.append(char) 

for char2 in list2:
    if char2 not in both_str1_and_str2_have:
        list2.append(char2)

print("Updated list1:", list1)
print("Updated list2:", list2)
