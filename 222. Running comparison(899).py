# cook your dish here
testcase=int(input())
while testcase>0:
    n=int(input())
    a=list(map(int , input().split()))
    b=list(map(int , input().split()))
    ans = 0 
    for i in range(n):
        if a[i]<=2*b[i] and b[i]<=2*a[i]:
            ans+=1 
    testcase-=1
    print(ans)
    