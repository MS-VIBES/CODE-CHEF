# cook your dish here
for _ in range(int(input())):
    r1,r2,r3=map(int,input().split())
    if (r1+r2)<r3:
        print("YES")
    elif (r2+r3)<r1:
        print("YES")
    elif (r1+r3)<r2:
        print("YES")
    else:
        print("NO")