# cook your dish here
n=int(input())
for i in range(n):
    l=list(map(int,input().split()))[:2]
    print((l[0]*7-l[1]))