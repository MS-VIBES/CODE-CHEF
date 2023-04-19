# cook your dish here
testcase=int(input())
while testcase>0:
    a,b,k=[int(k) for k in input().split()]
    steps=abs(b-a)
    if a == b:
        print("0")
    elif steps % k == 0:
        print(steps//k)
    else:
        print((steps//k)+1)
    testcase-=1