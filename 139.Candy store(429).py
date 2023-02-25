# cook your dish here
for _ in range(int(input())):
    chocolates_to_sell,chocolates_sold=map(int,input().split())
    profit_chocolates=chocolates_sold-chocolates_to_sell
    if (chocolates_sold<=chocolates_to_sell):
        print(chocolates_sold)
    else:
        print(chocolates_to_sell+(profit_chocolates*2))