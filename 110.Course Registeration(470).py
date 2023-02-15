for _ in range(int(input())):
    n,m,k=map(int,input().split())
    space=m-k
    if (space<n):
        print("NO")
    else:
        print("YES")