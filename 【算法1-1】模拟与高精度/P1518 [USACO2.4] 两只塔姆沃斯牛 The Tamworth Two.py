from typing import Tuple
_list = []
C_y = 0
C_x = 0
dir_C = [-1,0]
F_y = 0
F_x = 0
dir_F = [-1,0]
def change_dir(dir:Tuple[int, int])->Tuple[int, int]:
    if dir[0] == -1:
        return [0,1]
    if dir[1] == 1:
        return [1,0]
    if dir[0] == 1:
        return [0,-1]
    if dir[1] == -1:
        return [-1,0]

for i in range(10):
    map_str = input().strip()
    map_list = list(map_str)
    for j in range(len(map_str)):
        if map_list[j] == 'C':
            map_list[j] = '.'
            C_y = i
            C_x = j
        if map_list[j] == 'F':
            map_list[j] = '.'
            F_y = i
            F_x = j
    _list.append(map_list)

change_dir_flag = True
cnt = 0
while True:
    # print(f'C:{C_y} {C_x}  F:{F_y} {F_x}')
    change_dir_flag = True
    new_y = C_y + dir_C[0]
    new_x = C_x + dir_C[1]
    if 0<= new_y < 10 and 0<= new_x < 10:
        if _list[new_y][new_x] != '*':
        #     change_dir_flag = True
        # else:
            C_y += dir_C[0]
            C_x += dir_C[1]
            change_dir_flag = False
    if change_dir_flag:
        dir_C = change_dir(dir_C)
        
    change_dir_flag = True
    new_y = F_y + dir_F[0]
    new_x = F_x + dir_F[1]
    if 0<= new_y < 10 and 0<= new_x < 10:
        if _list[new_y][new_x] != '*':
            F_y += dir_F[0]
            F_x += dir_F[1]
            change_dir_flag = False
    if change_dir_flag:
        dir_F = change_dir(dir_F)

    cnt += 1
    if C_y == F_y and C_x == F_x:
        break
    if cnt > 10000:
        cnt = 0
        break
print(cnt)