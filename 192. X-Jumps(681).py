# cook your dish here
testcase=int(input())
while testcase>0:
    x,y=map(int,input().split())
    remainder=x%y
    if (x%y==0):
        print(x//y)
    else:
        print((x//y)+remainder)
    testcase-=1