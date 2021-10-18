island = int(input())
ls = [int(x) for x in input().split()]
a = 1
for i in range(0,island):
    print(ls[a-1])
    a += ls[a-1]

    if a < island :
        if i == island-1:
            print("No")
        continue
    else :
        print("Yes")
        break
