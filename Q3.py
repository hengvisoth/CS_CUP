n = int(input())
ls = [int(x) for x in input().split()]
res = 0
for i in ls :
    count = ls.count(i)
    if count %2 == 1 :
        res = i
print(res)
