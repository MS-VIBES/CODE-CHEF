# cook your dish here
test_case=int(input())
while test_case>0:
    police,thief=map(int,input().split())
    print(abs(police-thief))
    test_case-=1
    
