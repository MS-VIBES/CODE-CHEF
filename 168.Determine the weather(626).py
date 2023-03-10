# cook your dish here
for __ in range(int(input())):
    Pa,Pb,Qa,Qb=map(int,input().split())
    penalty_P=max(Pa,Pb)
    penalty_Q=max(Qa,Qb)
    if penalty_Q<penalty_P:
        print("Q")
    elif penalty_P<penalty_Q:
        print("P")
    else:
        print("TIE")