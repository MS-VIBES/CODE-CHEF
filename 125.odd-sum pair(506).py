# cook your dish here
t = int(input())
for i in range(t):
    a, b, c =map(int,input().split())
    if ((a+b) % 2 != 0 or ((b+c) % 2 != 0) or ((c+a) % 2 != 0)) :
        print("YES")
    else:
        print("NO")
