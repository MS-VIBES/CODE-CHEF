for _ in range(int(input())):
    x,y=map(int,input().split())
    double_room=x*3
    triple_room=y*2
    if (double_room>triple_room):
        print(triple_room)
    else:
        print(double_room)