'''
    输入一个不小于 100 且小于 1000,同时包括小数点后一位的一个浮点数，例如 123.4，要求把这个数字翻转过来，变成 
4.321 并输出。
'''

num = input().strip()
# print(num)
_num = [i for i in num]
_num.reverse()
# for i in range(len(_num)):
#     print(_num[i],end='')
ans = ''.join(_num)
print(ans)

