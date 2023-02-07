for _ in range(int(input())):
    x,y,z=map(int,input().split())
    five_coins=x*5
    ten_coins=y*10
    total_coins=five_coins+ten_coins
    print(total_coins//z)