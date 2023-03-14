for i in range(int(input())):
    a,b=input().split()
    a=int(a)
    b=int(b)
    f=0
    for j in range(2,a+b):
        if((a+b)%j==0):
            f=1
    if(f==1):
        print("Bob")
    else:
        print("Alice")