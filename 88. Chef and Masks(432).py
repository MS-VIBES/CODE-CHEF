# cook your dish here
for _ in range(int(input())):
    x,y = map(int,input().split())
    if x*100 == y*10:
        print('CLOTH')
    elif x*100 > y*10:
        print('CLOTH')
    else:
        print('DISPOSABLE')