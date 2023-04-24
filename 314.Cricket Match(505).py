testcase=int(input())
while testcase>0:
    n,m=[int(m) for m in input().split()]
    possible_overs = n/36
    print("NO") if possible_overs>m else print("YES")
    testcase-=1