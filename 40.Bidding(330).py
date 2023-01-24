# cook your dish here
for _ in range(int(input())):
    Alice,Bob,Charlie=map(int,input().split())
    if (Alice>Bob) and (Alice>Charlie):
        print("Alice")
    elif (Bob>Alice) and (Bob>Charlie):
        print("Bob")
    else:
        print("Charlie")