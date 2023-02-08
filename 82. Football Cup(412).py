for _ in range(int(input())):
    x,y=map(int,input().split())
    if (x==y):
        if(x!=0) and (y!=0):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")