# cook your dish here
for i in range(int(input())):
    x,y,z = map(int,input().split())
    time=0
    count=0
    while x:
        if count==3:
            time = time+z
            count = 0
        time = time + y
        x = x-1
        count +=1
    print(time)
        
