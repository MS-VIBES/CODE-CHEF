# cook your dish here
for _ in range(int(input())):
    alice,bob,charlie=map(int,input().split())
    least_value=min(alice,charlie,bob)
    max_value=max(alice,charlie,bob)
    flag=False
    for i in range(least_value,max_value+1):
        if i>=alice and i<=bob and i>=charlie:
            flag=True
            break
    if flag:
        print("YES")
    else:
        print("NO")