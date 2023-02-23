# cook your dish here
no_of_soldiers=int(input())
A=list(map(int,input().split()))
even=0
odd=0
for i in range(no_of_soldiers):
    if A[i]%2 == 0:
        even+=1
    else:
        odd+=1
if even>odd:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
