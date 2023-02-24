# cook your dish here
for _ in range(int(input())):
    cred_coins,number_of_bills=map(int,input().split())
    total_cred_coins=cred_coins*number_of_bills
    print(total_cred_coins//100)