testcase=int(input())
while testcase>0:
    n=int(input())
    s=input()
    lst=[]
    for i in s:
        if(i=='A'):
            lst.append('T')
        elif(i=='T'):
            lst.append('A')
        elif(i=='C'):
            lst.append('G')
        else:
            lst.append('C')
    for i in lst:
        print(i,end='')
    print()        
    testcase-=1
            

