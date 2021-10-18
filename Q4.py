n = int(input())
ls = [int(x) for x in input().split()]
num = 0
ans = 0
for i in ls :
    if i == 1 :
        num += 1
    else :
        num = 0
    ans = max(ans,num) # use this function to compare between answer and num

print(ans)
