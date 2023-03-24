# cook your dish here
testcase=int(input())
while testcase>0:
    x,y=map(int,input().split())
    fuel_needed=x*5
    print("No")if fuel_needed<y else print("Yes")
    testcase-=1
    
    
