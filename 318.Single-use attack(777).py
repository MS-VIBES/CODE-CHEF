import math
for _ in range(int(input())):
    h,x,y=map(int,input().split())
    if (x>=y):
        print(math.ceil(h/x))
    else:
        print(math.ceil((h-y)/x)+1)