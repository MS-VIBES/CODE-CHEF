for _ in range(int(input())):
    fours=0
    num=input()
    for i in num:
        if i == "4":
            fours+=1
    print(fours)
