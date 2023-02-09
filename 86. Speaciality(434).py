t = int(input())
for i in range(t):
    x,y,z = map(int,input().split())
    if (x>y):
        if(x>z):
            print("Setter")
            continue
    if (y>x):
        if(y>z):
            print("Tester")
            continue
    if (z>x):
        if(z>y):
            print("Editorialist")
            continue