import math
for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    alex_dist=math.sqrt((a**2)+(b**2))
    Bob_dist=math.sqrt((c**2)+(d**2))
    if alex_dist > Bob_dist:
        print("Alex")
    elif Bob_dist >alex_dist:
        print("Bob")
    else:
        print("equal")