# cook your dish here
import math
for _ in range(int(input())):
    total_friends,cost_of_each_subs=map(int,input().split())
    subscription=math.ceil(total_friends/6)
    print(subscription*cost_of_each_subs)
        
