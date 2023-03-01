# cook your dish here
for _ in range(int(input())):
    n=int(input())
    total_income=n*50
    amount_spend=(total_income*.20)+(total_income*.20)+(total_income*.30)
    profit=total_income-amount_spend
    print(int(profit))