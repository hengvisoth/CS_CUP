ls = [int(x) for x in input().split()]
n = ls[0]
m = ls[1]
k = ls[2]
c = ls[3]
money_recieve = (n//m) * k
res = n + money_recieve//c
print(res)
