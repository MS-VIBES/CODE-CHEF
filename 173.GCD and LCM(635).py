# cook your dish here
import math
for _ in range(int(input())):
    a,b=map(int,input().split())
    print(math.gcd(a,b),math.lcm(a,b))


