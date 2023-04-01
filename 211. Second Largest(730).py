# cook your dish here
testcase=int(input())
while testcase>0:
    s=[int(s) for s in input().split()]
    s.sort()
    testcase-=1
    print(s[1])