from typing import List
from abc import ABC, abstractmethod
# def judge_90(sour_arr:List,tar_arr:List)->bool:
# 使得该类不能被实例化
class BaseJudge(ABC):
    def __init__(self,sour_arr:List,tar_arr:List) -> None:
        super().__init__()
        self.sour_arr = sour_arr
        self.tar_arr = tar_arr
        self.bool_flag = False
    # 使得该类被继承时一定要实现抽象方法
    @abstractmethod
    def judge(self)->bool:
        pass
class Judge90(BaseJudge):
    def judge(self) -> bool:
        for i in range(len(self.sour_arr)):
            for j in range(len(self.sour_arr)):
                if self.sour_arr[i][j] != self.tar_arr[j][len(self.sour_arr)-1-i]:
                    return self.bool_flag
        self.bool_flag = True
        return self.bool_flag
class Judge180(BaseJudge):
    def judge(self) -> bool:
        for i in range(len(self.sour_arr)):
            for j in range(len(self.sour_arr)):
                if self.sour_arr[i][j] != self.tar_arr[len(self.sour_arr)-1-i][len(self.sour_arr)-1-j]:
                    return self.bool_flag
        self.bool_flag = True
        return self.bool_flag
class Judge270(BaseJudge):
    def judge(self) -> bool:
        for i in range(len(self.sour_arr)):
            for j in range(len(self.sour_arr)):
                if self.sour_arr[i][j] != self.tar_arr[len(self.sour_arr)-1-j][i]:
                    return self.bool_flag
        self.bool_flag = True
        return self.bool_flag
class Judge_plane(BaseJudge):
    def judge(self) -> bool:
        for i in range(len(self.sour_arr)):
            for j in range(len(self.sour_arr)):
                if self.sour_arr[i][j] != self.tar_arr[i][len(self.sour_arr)-1-j]:
                    return self.bool_flag
        self.bool_flag = True
        return self.bool_flag
class Judge_prim(BaseJudge):
    def judge(self) -> bool:
        for i in range(len(self.sour_arr)):
            for j in range(len(self.sour_arr)):
                if self.sour_arr[i][j] != self.tar_arr[i][j]:
                    return self.bool_flag
        self.bool_flag = True
        return self.bool_flag

n = int(input().strip())
primary_arr = []
for i in range(n):
    primary_arr.append(input().strip())
final_arr = []
for i in range(n):
    final_arr.append(input().strip())
assert len(primary_arr) == len(final_arr), print('the size of two matrix are not equel')

new_arr = [i[::-1] for i in primary_arr]
# print(new_arr)

if Judge90(sour_arr=primary_arr,tar_arr=final_arr).judge():
    print(1)
elif Judge180(sour_arr=primary_arr,tar_arr=final_arr).judge():
    print(2)
elif Judge270(sour_arr=primary_arr,tar_arr=final_arr).judge():
    print(3)
elif Judge_plane(sour_arr=primary_arr,tar_arr=final_arr).judge():
    print(4)
elif Judge90(sour_arr=new_arr,tar_arr=final_arr).judge() or Judge180(sour_arr=new_arr,tar_arr=final_arr).judge() or Judge270(sour_arr=new_arr,tar_arr=final_arr).judge():
    print(5)
elif Judge_prim(sour_arr=primary_arr,tar_arr=final_arr).judge():
    print(6)
else:
    print(7)
