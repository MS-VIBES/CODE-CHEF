# cook your dish here
for _ in range(int(input())):
    people_at_party,tiles_available=map(int,input().split
    ())
    print("YES") if tiles_available%people_at_party==0 else print("NO")
    