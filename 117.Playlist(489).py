# cook your dish here
for _ in range(int(input())):
    train_minutes,song_duration=map(int,input().split())
    one_loop_duration=song_duration*3
    print(train_minutes//one_loop_duration)