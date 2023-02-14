p1,p2,p3,p4=map(int,input().split())

count=0
l=[p1,p2,p3,p4]
for i in l:
    if i>=10:
        count+=1
print(count)