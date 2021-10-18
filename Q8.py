num = (input())
a = ""
ls = []
try :
    dislike = (input())
except :
    dislike= ""
if dislike == "":
    for j in range(0,len(num)) :
        for k in range(j,len(num)):
            a += num[k]
            ls.append(a)
        a = ""
else :
    for i in dislike :
        num = num.replace(i," ")
    number = num
    # problem with loop
    for j in range(0,len(number)) :
        if number[j] == " ":
            continue

        for k in range(j,len(number)):
            if number[k] == " ":
                break
            a += number[k]
            ls.append(a)
        a = ""
print(len(ls))
