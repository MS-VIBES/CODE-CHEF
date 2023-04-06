testcase=int(input())
while testcase>0:
    x,y=[int(x) for x in input().split()]
    testcase-=1
    print(abs(x-y))