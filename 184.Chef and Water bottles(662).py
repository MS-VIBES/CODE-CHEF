# cook your dish here
testcase=int(input())
while testcase>0:
    n,x,k=map(int,input().split())
    no_of_water_bottles=k//x
    if (no_of_water_bottles>=n):
        print(n)
    else:
        print(no_of_water_bottles)
    testcase-=1