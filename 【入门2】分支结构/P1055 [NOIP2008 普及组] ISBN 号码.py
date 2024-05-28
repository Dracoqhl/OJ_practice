num_list = input().split('-')
# print(num_list)
num_str = ''.join(num_list[:-1])
# print(num_str)
ans = 0
for i in range(len(num_str)):
    ans += int(num_str[i])*(i+1)
# print(ans)
ans = ans % 11
# print(ans)
bit = str(ans)
if ans == 10:
    bit = 'X'
if bit == num_list[-1]:
    print('Right')
else:
    num_list[-1] = bit
    print('-'.join(num_list))