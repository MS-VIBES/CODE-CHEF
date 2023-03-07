# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    a_investment=(a*10)
    b_inestment=(b*5)
    if (a_investment>b_inestment):
        print("FIRST")
    elif (a_investment<b_inestment):
        print("SECOND")
    else:
        print("ANY")