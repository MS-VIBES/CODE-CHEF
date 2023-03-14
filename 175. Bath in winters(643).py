# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    per_person_water=y*2
    print(0 if per_person_water>x else x//per_person_water)