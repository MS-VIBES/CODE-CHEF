# cook your dish here
testcase=int(input())
while testcase>0:
    n,k,m=map(int,input().split())
    per_bag_candies=k*m
    if (n%per_bag_candies==0):
        print(n//per_bag_candies)
    else:
        print((n//per_bag_candies)+1)
    testcase-=1