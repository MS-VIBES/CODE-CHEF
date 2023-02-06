for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    lst=[]
    for i in range(a,b+1):
        lst.append(i)
    for j in range(c,d+1):
        lst.append(j)
    print(len(set(lst)))
