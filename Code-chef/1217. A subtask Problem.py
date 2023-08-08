# cook your dish here
t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    l=list(map(int,input().split()))
    if sum(l)==n:
        print(100)
    else:
        if sum(l[:m])==m:
            print(k)
        else:
            print(0)