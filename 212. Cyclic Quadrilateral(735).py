# cook your dish here
testcase=int(input())
while testcase>0:
    a,b,c,d=[int(d) for d in input().split()]
    if (a+c)==(b+d)==180:
        print("YES")
    else:
        print("NO")
    testcase-=1