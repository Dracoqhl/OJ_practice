num = int(input().strip())
sum = 0
score_list = input().split(' ')
score_list = [int(i) for i in score_list]
for i in score_list:
    sum += int(i)
max_num = max(score_list)
min_num = min(score_list)
ans = (sum-max_num-min_num) /(num-2)
print(f'{ans:.2f}')