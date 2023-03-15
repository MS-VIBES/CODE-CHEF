# cook your dish here
testcase=int(input())
while testcase>0:
    x,y=map(int,input().split())
    rating_needed=y-x
    if(rating_needed)%8==0:
        print(rating_needed//8)
    else:
        print((rating_needed)//8+1)
    testcase-=1
        

        
