# cook your dish here
for _ in range(int(input())):
    n,m,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    
    first=0
    second=0
    for i in range(1,n+1):
        if i in a and i in b:
            first+=1 
        elif i not in a and i not in b:
            second+= 1 
    print(str(first)+" "+ str(second))