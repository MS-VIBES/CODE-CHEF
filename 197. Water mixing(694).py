# cook your dish here
testcase=int(input())
while testcase>0:
    a,b,x,y=map(int,input().split())
    diff=abs(a-b)
    if (a<b):
        if diff <= x:
            print("Yes")
        else:
            print("No")
    elif (a>b):
        if diff <= y:
            print("yes")
        else:
            print("no")
    else:
        print("yes")
    tescase-=1