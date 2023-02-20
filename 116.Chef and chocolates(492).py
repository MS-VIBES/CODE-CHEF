# cook your dish here
for _ in range(int(input())):
    target,available,cost=map(int,input().split())
    chocolates_to_buy=target-available
    print(chocolates_to_buy*cost)