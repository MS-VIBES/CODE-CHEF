# cook your dish here
for _ in range(int(input())):
    initial_a,initial_b=map(int,input().split())
    final_a,final_b=map(int,input().split())
    if (final_a>=initial_a) and (final_b>=initial_b):
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")