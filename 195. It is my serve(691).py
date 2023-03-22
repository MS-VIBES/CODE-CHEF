# cook your dish here
testcase=int(input())
while testcase>0:
    p,q=map(int,input().split())
    if(p+q)%4==0 or (p+q)%4==1:
        print("Alice")
    else:
        print("Bob")
    testcase-=1