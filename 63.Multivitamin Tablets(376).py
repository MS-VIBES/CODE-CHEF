for _ in range(int(input())):
    x,y=map(int,input().split())
    tablets=x*3
    if y>=tablets:
        print("YES")
    else:
        print("NO")