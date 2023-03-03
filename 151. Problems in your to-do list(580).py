# cook your dish here
for _ in range(int(input())):
    n=int(input())
    D=list(map(int,input().split()))
    count=0
    for i in range(n):
        if D[i]>=1000:
            count+=1
            continue
    print(count)
                  

 