# cook your dish here
testcase=int(input())
while testcase>0:
    a,b=map(int,input().split())
    third_no=abs(21-(b+a))
    if (third_no>=1) and (third_no<=10):
        print(third_no)
    else:
        print(-1)
    testcase-=1