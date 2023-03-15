test_cases=int(input())
while test_cases>0:
    x=int(input())
    if (x%3==0):
        print("Normal")
    elif(x%3 == 2):
        print("Small")
    else:
        print("Huge")
    test_cases-=1
    
    
  