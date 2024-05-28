import math
import numpy as np
N = int(input().split()[0])
# N = map(int,input().split())
price_list = []
for i in range(3):
    num, price = map(int,input().split())
    n = math.ceil(N/num)
    price_list.append(n*price)

print(min(price_list))
