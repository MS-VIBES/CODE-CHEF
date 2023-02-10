for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    if (a-c)>(b-d):
        print("Second")
    elif (b-d)>(a-c):
        print("First")
    else:
        print("Any")