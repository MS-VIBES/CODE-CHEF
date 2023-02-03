for _ in range(int(input())):
    n,x,y=map(int,input().split())
    pages_read=x*y
    if pages_read<n:
        print("NO")
    else:
        print("YES")