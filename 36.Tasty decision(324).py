for i in range(int(input())):
    n=int(input())
    sum=0
    j=1
    while (n>0):
       sum+=1
       j+=1
       n-=j
    print(sum)