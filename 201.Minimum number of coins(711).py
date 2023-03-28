# cook your dish here
testcase=int(input())
while testcase>0:
    x=int(input())
    if (x%10==0):
        print(x//10)
    elif(x%10!=0 and x%5==0):
        print((x//10)+1)
    else:
        print(-1)
    testcase-=1