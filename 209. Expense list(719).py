# cook your dish here
testcase=int(input())
while testcase>0:
    n,x=[int(x) for x in input().split()]
    total_income=2**x
    for i in range(n):
        total_income=total_income-(total_income//2)
    testcase-=1
    print(total_income)