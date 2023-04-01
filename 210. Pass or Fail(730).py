# cook your dish here
testcase=int(input())
while testcase>0:
    n,x,p=map(int,input().split())
    correct_marks=x*3
    total_marks=correct_marks-(n-x)
    print("FAIL" if total_marks<p else "PASS")
    testcase-=1