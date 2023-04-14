for _ in range(int(input())):
    x,y=map(int,input().split())
    dist_covered=x*15
    total_distance=y*2
    if total_distance > dist_covered:
        print("No")
    else:
        print("yes")