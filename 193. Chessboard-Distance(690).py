# cook your dish here
testcase=int(input())
while testcase>0:
    x1,y1,x2,y2=map(int,input().split())
    print(max(abs(x1-x2),abs(y1-y2)))
    testcase-=1
    
 