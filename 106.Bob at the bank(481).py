# cook your dish here
for _ in range(int(input())):
    w,x,y,z=map(int,input().split())
    final_salary=x*z 
    final_deducted=y*z
    left_amount=final_salary-final_deducted
    print(w+left_amount)