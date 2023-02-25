# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    alice_avg=400/x
    bob_avg=400/y
    charlie_avg=400/z
    if alice_avg>bob_avg and alice_avg>charlie_avg:
        print("ALICE")
    elif bob_avg>alice_avg and bob_avg>charlie_avg:
        print("BOB")
    else:
        print("CHARLIE")