# cook your dish here
testcase=int(input())
while testcase>0:
    a,x,b,y=map(int,input().split())
    alice_speed=a/x
    bob_speed=b/y
    if (alice_speed>bob_speed):
        print("alice")
    elif (alice_speed<bob_speed):
        print("bob")
    else:
        print("equal")
    testcase-=1