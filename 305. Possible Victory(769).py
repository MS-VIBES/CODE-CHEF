R,O,C=map(int,input().split())
overs_left=20-O
max_score_possible=overs_left * 6*6
total_max_score_possible=max_score_possible + C 
if R <  total_max_score_possible:
    print("NO")
else:
    print("YES")