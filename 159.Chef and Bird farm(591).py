
for _ in range(int(input())):
    chicken_legs,duck_legs,total_legs=map(int,input().split())
    if total_legs%chicken_legs==0 and total_legs%duck_legs==0:
        print("ANY")
    elif total_legs%duck_legs==0:
        print("DUCK")
    elif total_legs%chicken_legs==0:
        print("CHICKEN")
    else:
        print("NONE")