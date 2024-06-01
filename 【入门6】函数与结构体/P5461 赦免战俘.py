import numpy as np
import math

def judge(arr:np.array,x:int,y:int,dis:int):
    if dis >=1:
        # judge(arr,x,x + ((xx - x)/2),y,y+(yy-y)//2)
        # judge(x,y,dis//2)
        judge(arr,x+dis//2,y,dis//2)
        judge(arr,x,y+dis//2,dis//2)
        judge(arr,x+dis//2,y+dis//2,dis//2)
    for i in range(dis//2):
        for j in range(dis//2):
            arr[x+i][y+j] = 0

num = int(input().strip())
ans_arr = np.ones((2**num,2**num))
# print(ans_arr)
judge(ans_arr,0,0,2**num)
for i in ans_arr:
    num_str_list = [str(int(j)) for j in i]
    print(' '.join(num_str_list))
    # print(num_str_list)
# print(ans_arr)

