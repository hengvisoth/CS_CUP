
n = int(input())
ls = [int(x) for x in input().split()]

res = 0
i = 0
j = n-1
alice = 0
bob = 0
while i <= j :
    res = ls[0] - ls[n-1]
    if len(ls) == 1 and ls[0]!= 0 :
        if alice > bob :
            bob+=1
            ls.pop(0)
            break
        elif alice < bob :
            alice +=1
            ls.pop(0)
            break
    if ls[0] == 0:
        ls.pop(0)
        n-=1

    if ls[n-1] == 0:
        ls.pop(n-1)
        n-=1

    if len(ls) == 1 :
        if alice > bob :
            bob+=1
            ls.pop(0)
            break
        elif alice < bob :
            alice +=1
            ls.pop(0)
            break

    if res == 0 :
        ls.pop(0)
        n -=1
        alice +=1

        ls.pop(n-1)
        n -=1
        bob += 1
    elif res < 0 :
        ls.pop(0)
        alice+=1
        n-=1
        ls[n-1] = abs(res)



    elif res > 0 :
        ls.pop(n-1)
        bob +=1
        n-=1
        ls[0] = abs(res)


res_alice = alice
res_bob = bob

print(res_alice,res_bob)
if res_alice > res_bob :
    print("Alice")
else :
    print("Bob")
