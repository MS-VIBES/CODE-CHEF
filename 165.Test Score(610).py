# cook your dish here
for _ in range(int(input())):
    n,x,y=map(int,input().split())
    if n*x >= y and y%x == 0:
        print("YES")
    else:
        print("NO")