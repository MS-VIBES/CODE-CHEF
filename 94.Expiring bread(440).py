for _ in range(int(input())):
    n,m,k=map(int,input().split())
    max_bread=m*k 
    if (n<=max_bread):
        print("YES")
    else:
        print("NO")