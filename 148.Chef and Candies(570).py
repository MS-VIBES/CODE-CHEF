# cook your dish here
import math
for _ in range(int(input())):
    no_of_children,candies_available=map(int,input().split())
    candies_to_buy=no_of_children-candies_available
    if candies_to_buy>0:
        packets_to_buy=candies_to_buy/4
        print(math.ceil(packets_to_buy))
    else:
        print(0)