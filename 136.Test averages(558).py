# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    d=((a+b)/2)
    e=((b+c)/2)
    f=((c+a)/2)
    if (d<35 or e<35 or f<35):
        print("Fail")
    else:
        print("Pass") 