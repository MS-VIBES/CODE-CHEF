# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    total=a+b+c 
    if (total>=6):
        print("YES")
    else:
        print("NO")