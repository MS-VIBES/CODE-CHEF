# cook your dish here
for _ in range(int(input())):
    x=int(input())
    questions_attempted=x%3
    if (questions_attempted%3)==0:
        print(questions_attempted)
    else:
        print(3-questions_attempted%3)