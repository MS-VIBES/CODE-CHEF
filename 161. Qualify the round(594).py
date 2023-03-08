# cook your dish here

for i in range(int(input())):
        x,a,b=map(int,input().split())
        print("Qualify") if (a+2*b>=x) else print("Notqualify")