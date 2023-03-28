# cook your dish here
testcase=int(input())
while testcase>0:
    n=int(input())
    a=[int(a)for a in input().split()]
    count=0
    for i in a:
        if a[i]>=10 and a[i]<=60:
            count+=1
        else:
            continue
    testcase-=1
    print(count)