# cook your dish here
testcase=int(input())
while testcase>0:
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    count=0
    for i in range(n):
        if a[i] >= x:
            count+=1 
        else:
            continue
    testcase-=1
    print(count)