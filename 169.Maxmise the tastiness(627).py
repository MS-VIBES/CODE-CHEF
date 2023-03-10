# cook your dish here
for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    max_first=max(a,b)
    max_second=max(c,d)
    print(max_second+max_first)