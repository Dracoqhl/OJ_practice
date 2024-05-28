import numpy as np
num = int(input().strip())
ans_arr = np.zeros([num,num])
# print(ans_arr)
pos_x = num//2
pos_y = 0
ans_arr[pos_y,pos_x] = 1
# print(ans_arr)
for i in range(2,num**2+1):
    if pos_y == 0 and pos_x != num-1:
        pos_y = num-1
        pos_x += 1
    elif  pos_y != 0 and pos_x == num-1:
        pos_y -= 1
        pos_x = 0
    elif pos_y == 0 and pos_x == num-1:
        pos_y +=1
        # pos_x = 0
    elif pos_y != 0 and pos_x != num-1:
        if ans_arr[pos_y-1,pos_x+1] == 0:
            pos_y -= 1
            pos_x += 1
        else:
            pos_y += 1
    ans_arr[pos_y,pos_x] = i
    # print(ans_arr)
    # print(f'{pos_y}  {pos_x}')
# print(ans_arr)
for i in range(num):
    for j in range(num):
        print(f'{ans_arr[i,j]:.0f}',end=' ')
    print('')