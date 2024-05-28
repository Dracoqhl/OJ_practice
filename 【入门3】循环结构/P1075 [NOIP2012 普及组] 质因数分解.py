import typing
import math
import time
def is_prim(num:int)->bool:
    end_n = int(math.sqrt(num))
    prim_flag = True
    if num == 2:
        return prim_flag
    for i in range(2,num+1):
        if i > end_n:
            break
        if num % i == 0:
            prim_flag = False
            break
    return prim_flag

num = int(input().strip())
'''
    new version:既然是成对出现的，所以较小的质数必然对应着最大的质数,同时两个质数的乘积必然不可能有其余的因数，
    故只要找到一个因数即可，完全不用判断是否为素数 =.=
'''
for i in range(2,num):
    if num%i == 0:
        print(num//i)
        break

''''
    The time out version
'''
# start_time = time.time()
# for i in range(num,2,-1):
#     if num%i == 0 and is_prim(i):
#         print(i)
#         break
# num_time = time.time()-start_time
# print(num_time)




        