import sys

a,b,c = map(int,input().split())
_a = min(a,b,c)
_c = max(a,b,c)
_b = a+b+c-_a-_c
# print(_a,_b,_c)
if _a + _b <= _c:
    print('Not triangle')
    sys.exit()
if _a**2+_b**2 == _c**2:
    print('Right triangle')
if _a**2+_b**2 > _c**2:
    print('Acute triangle')
if _a**2+_b**2 < _c**2:
    print('Obtuse triangle')
if _a == _b or _b ==_c or _a == _c:
    print('Isosceles triangle')
# 等腰三角形一定是等边
if _a == _b and _a == _c :
    print('Equilateral triangle')