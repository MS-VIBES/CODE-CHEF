# cook your dish here
testcase=int(input())
while testcase>0:
    x,y,z=map(int,input().split())
    time_to_reach=y//x
    min_time=z-time_to_reach
    if time_to_reach<z:
        print(min_time)
    else:
        print(0)
    testcase-=1