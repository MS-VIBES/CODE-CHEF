# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    min_of_two=min(b,c)
    p=b-min_of_two
    q=c-min_of_two
    sum=p+q
    if a!=0 and a> sum:
        print("YES")
    else:
        print("NO")