# cook your dish here
testcase=int(input())
while testcase>0:
    x,y=map(int,input().split())
    if x<y:
        print(0)
    else:
        print(x//y)
    testcase-=1