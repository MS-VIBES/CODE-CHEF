# cook your dish here
testcase=int(input())
while testcase>0:
    n=int(input())
    print((n//10) if (n%10==0) else ((n//10)+1))
    testcase-=1