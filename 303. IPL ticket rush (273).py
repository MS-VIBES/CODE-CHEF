testcase=int(input())
while testcase > 0:
    n,m=[int(m) for m in input().split()]
    print(0) if m>=n else print(abs(m-n))
    testcase-=1