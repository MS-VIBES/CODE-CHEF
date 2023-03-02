# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    if (a+b)%2 ==0:
        print ((a+b)//2) 
    else: 
        print ("-1")