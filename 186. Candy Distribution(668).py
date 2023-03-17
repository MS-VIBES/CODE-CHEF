for _ in range(int(input())):
    n,m=map(int,input().split())
    candies=n//m
    if (candies%2==0) and (n%m==0):
        print("Yes")
    else:
        print("No")