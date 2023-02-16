# cook your dish here
for _ in range(int(input())):
    initial_water,capacity,rate,time=map(int,input().split())
    inflow=initial_water+(rate*time)
    if inflow>capacity:
        print("Overflow")
    elif (inflow<capacity):
        print("Unfilled")
    else:
        print("filled")