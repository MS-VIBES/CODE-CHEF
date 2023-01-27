# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    total_passes=n+1
    if k>=total_passes:
        print("YES")
    else:
        print("NO")