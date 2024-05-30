_dic = {}
_alph = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in _alph:
    _dic[i] = 0
# print(len(_alph))
for i in range(4):
    _str = input().strip()
    for i in _str:
        if i not in _alph:
            continue
        if i in _dic:
            _dic[i] += 1

# print(_dic)
max_snt = max(_dic.values())
# print(max_snt)
for i in range(max_snt,0,-1):
    tem_list = []

    for j in _alph:
        if _dic[j] >= max_snt:
            tem_list.append('*')
        else:
            tem_list.append(' ')
    ans_str = ' '.join(tem_list)
    print(f'{ans_str}')
    max_snt -= 1
print(' '.join(_alph))