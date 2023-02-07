for _ in range(int(input())):
    x,y=map(int,input().split())
    if y*10 >= x:
        print("NO")
    else:
        print("YES")