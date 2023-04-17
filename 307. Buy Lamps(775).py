for i in range(int(input())):
    n,k,x,y=map(int,input().split())
    if n==k:
        print(n*x)
    else:
        a=(n-k)*y+k*x
        b=(n-k)*x+k*x
        print(min(a,b))