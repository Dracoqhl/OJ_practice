n,m = map(int,input().split())
# print(n,m)
score = []
for i in range(n):
    score_list = input().split()
    score_list = [int(i) for i in score_list]
    _sum = sum(score_list)
    _max = max(score_list)
    _min = min(score_list)
    score.append((_sum-_max-_min)/(m-2))
# print(score)
print(f'{max(score):.2f}')