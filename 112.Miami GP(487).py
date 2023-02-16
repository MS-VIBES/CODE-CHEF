for _ in range(int(input())):
    fastest_time,chef_time=map(int,input().split())
    time_expected=fastest_time*(1.07)
    if (chef_time<=time_expected):
        print("YES")
    else:
        print("NO")