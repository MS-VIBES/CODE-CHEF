# cook your dish here
for _ in range(int(input())):
    n,x,y=map(int,input().split())
    total_size=x+y*2
    if (total_size<=n):
        print("YES")
    else:
        print("NO")