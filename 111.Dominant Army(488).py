# cook your dish here
for t in range(int(input())):
    na,nb,nc = map(int,input().split())
    c = 0
    if(na>(nc+nb)):
        c = 1 
    elif(nb>(nc+na)):
        c = 1 
    elif(nc>(na+nb)):
        c = 1 
    if(c==1):
        print("Yes")
    else:
        print("No")