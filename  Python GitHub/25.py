text = str(input())

count_of_a01c = 0

for subtext in text:
    if subtext == "a01c" :
        count_of_a01c += 1
        if count_of_a01c >= 3 :
             text.replace(" ","")
             print (text)
    else :
        text.center(text.len(),"-")
        print(text)
