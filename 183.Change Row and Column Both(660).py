
test_case=int(input())
while test_case>0:
    sx,sy,ex,ey=map(int,input().split())
    if (sx!=ex) and (sy!=ey):
        print(1)
    else:
        print(2)
    test_case-=1