import math
input_str = input().strip()
_dic = {}
def is_prim(num:int)->bool:
    end_n = int(math.sqrt(num))
    prim_flag = True
    if num <= 1:
        return False
    if num == 2:
        return prim_flag
    for i in range(2,num+1):
        if i > end_n:
            break
        if num % i == 0:
            prim_flag = False
            break
    return prim_flag
for i in input_str:
    if i in _dic:
        _dic[i] += 1
    else:
        _dic[i] = 1
# print(_dic)
dis = max(_dic.values()) - min(_dic.values())
# print(f'dis:{dis}')
if is_prim(dis):
    print('Lucky Word')
    print(dis)
else:
    print('No Answer')
    print('0')

