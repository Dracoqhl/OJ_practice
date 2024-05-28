'''
    python写高精度没啥意思，因为不涉及这个问题
'''
import math
num = int(input().strip())
sum = 0
for i in range(1,num+1):
    sum += math.factorial(i)
print(sum)