n = int(input())
ls = [int(x) for x in input().split()]
a = ls[0]
b = ls[1]
c = ls[2]
ls = [c, c, a, c, b, a, c]
day = 0
if c < a and c < b:
    i = -1
    while True:

        n = n - ls[i]
        if n < 0 :
            break
        day += 1
        i += 1
        if i == 7:
            i = 0
       
elif a < b and a < c:
    i = -2
    while True:

        n = n - ls[i]
        if n < 0:
            break
        day += 1
        i += 1
        if i == 7:
            i = 0
    
elif b < a and b < c:
    i = 4
    while True:

        n = n - ls[i]
        if n < 0:
            break
        day += 1
        i += 1
        if i == 7:
            i = 0

print(day )


