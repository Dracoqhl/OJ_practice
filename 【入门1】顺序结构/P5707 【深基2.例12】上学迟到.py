'''
    学校和 yyy 的家之间的距离为 𝑠 米，而 yyy 以 𝑣 米每分钟的速度匀速走向学校。
    在上学的路上，yyy 还要额外花费 10 分钟的时间进行垃圾分类。
    学校要求必须在上午 8:00 到达，请计算在不迟到的前提下，yyy 最晚能什么时候出门。
    由于路途遥远，yyy 可能不得不提前一点出发，但是提前的时间不会超过一天。
'''
s,v = map(int,input().split())
t = s//v
# print('t:',t)
if s > t*v:
    t = t+1+10
else:
    t = t+10
h = t // 60
m = t%60
# print(h,m)

if m >= 0:
    m = 60-m
    h = 8-h-1
else:
    m = 0
    h = 8-h
if h <0:
    h = h + 24
print(f'{h:02}:{m:02}')
