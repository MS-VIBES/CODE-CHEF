for _ in range(int(input())):
    x,y=map(int,input().split())
    buying_price=x-y
    selling_price=x + (x*10)//100
    profit=selling_price-buying_price
    print(profit)