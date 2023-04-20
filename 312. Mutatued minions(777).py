#method-I
testcase=int(input())
while testcase>0:
    n,k = map(int,input().split())
    minions = [int(a) for a in input().split()]
    count=sum(1 for minion in minions if (minion +k)%7 == 0)
    testcase-=1
    print(count)
  
#Method-II
# cook your dish h(ere
testcase=int(input())
while testcase>0:
    n,k = map(int,input().split())
    a = [int(a) for a in input().split()]
    count = 0
    for j in range(n):
        if((a[j]+k)%7==0):
            count = count+1
    testcase-=1
    print(count)
  
    