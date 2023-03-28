# cook your dish here
testcase=int(input())
while testcase>0:
    x,y,d=[int(x)for x in input().split()]
    print("YES")  if (abs(x-y)<=d) else print("NO")
    testcase-=1
    
    
    