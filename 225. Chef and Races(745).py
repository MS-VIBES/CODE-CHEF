# cook your dish here
for _ in range(int(input())):
    x,y,a,b=map(int,input().split())
    if (x==a or x==b) and (y==a or y==b):
        print("0")
    elif (x==a or x==b) or(y==b):
        print("1")
    else:
        print("2")