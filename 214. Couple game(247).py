testcase=int(input())
while testcase>0:
    g,b=[int(a) for a  in input().split()]
    print(abs(g-b))
    testcase-=1