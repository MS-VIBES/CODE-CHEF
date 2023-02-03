for _ in range(int(input())):
    n,x,k=map(int,input().split())
    total_cost=n*x 
    if total_cost<=k:
        print("YES")
    else:
        print("NO")