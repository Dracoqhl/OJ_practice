import math
def is_prim(num:int)->bool:
    end_n = int(math.sqrt(num))
    prim_flag = True
    if num < 2:
        prim_flag = False
        return prim_flag
    if num == 2:
        return prim_flag
    for i in range(2,num+1):
        if i > end_n:
            break
        if num % i == 0:
            prim_flag = False
            break
    return prim_flag

num = int(input())
num_list = input().split()
num_list = [int(i) for i in num_list]
# print(num_list)
ans_list = [str(i) for i in num_list if is_prim(i)]
print(' '.join(ans_list))
