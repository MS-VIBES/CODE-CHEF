# cook your dish here
for _ in range(int(input())):
    chef,chefina=map(int,input().split())
    if (chef+chefina)>6:
        print("YES")
    else:
        print("NO")