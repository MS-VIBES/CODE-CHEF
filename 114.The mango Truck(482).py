# cook your dish here
for _ in range(int(input())):
    mango,truck,max_weigh=map(int,input().split())
    left_weigh=max_weigh-truck
    print(left_weigh//mango)
    