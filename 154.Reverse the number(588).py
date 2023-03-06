

for _ in range(int(input())):
    reverse=0
    num=int(input())
    while num>0:
        remainder=num%10
        reverse=reverse*10+remainder
        num=int(num/10)
    print(reverse)

