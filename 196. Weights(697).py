# cook your dish here
testcase=int(input())
while testcase>0:
    w,x,y,z=map(int,input().split())
    if w==x or w==y or w==z:
        print("yes")
    elif w==(x+y) or w==(y+z) or w==(z+x) or w==(x+y+z):
        print("yes")
    else:
        print("no")
    testcase-=1