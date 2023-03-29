# cook your dish here
import math
testcase=int(input())
while testcase>0:
    x,y=[int(y)for y in input().split()]
    floor_A=math.ceil(x/10)
    floor_B=math.ceil(y/10)
    print(abs(floor_A-floor_B))
    testcase-=1