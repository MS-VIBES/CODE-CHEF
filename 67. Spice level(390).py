for _ in range(int(input())):
    x=int(input())
    if x<4:
        print("MILD")
    elif x>=4 and x<7:
        print("MEDIUM")
    else:
        print("HOT")