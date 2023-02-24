# cook your dish here
import math
for _ in range(int(input())):
    friends,slices_needed=map(int,input().split())
    total_slice_needed=slices_needed*friends
    ans=total_slice_needed/4
    print(math.ceil(ans))