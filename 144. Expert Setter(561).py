# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    half=x/2
    if (y>=half):
        print("YES")
    else:
        print("NO")