#FOR LOOPS
# cook your dish here
for _ in range(int(input())):
    date=input()
    x=len(date)
    one=int(date[0:2])
    two=int(date[3:5])
    if one>12 and two<=12:
        print("DD/MM/YYYY")
    elif one<=12 and two>12:
        print("MM/DD/YYYY")
    else:
        print("BOTH")