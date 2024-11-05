string = "and anc fhg dk aa ss aaa adnef"

string_new = string.split()

result = []

def first_letter_a(words):
    for i in words:
        if(i.startswith('a')):
            result.append(i)
    return result
print(first_letter_a(string_new))