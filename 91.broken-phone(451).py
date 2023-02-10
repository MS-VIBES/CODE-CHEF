for _ in range(int(input())):
    x,y=map(int,input().split())
    if (x>y):
        print("NEW PHONE")
    elif (x<y):
        print("REPAIR")
    else:
        print("ANY")