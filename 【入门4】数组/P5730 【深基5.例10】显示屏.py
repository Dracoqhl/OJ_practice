'''
    没有必要多嵌套一层方括号，但是懒得改了
'''
num = int(input().strip())
num_str = input().strip()
num_dic = {
    '0': [['XXX'],['X.X'],['X.X'],['X.X'],['XXX']],
    '1': [['..X'],['..X'],['..X'],['..X'],['..X']],
    '2': [['XXX'],['..X'],['XXX'],['X..'],['XXX']],
    '3': [['XXX'],['..X'],['XXX'],['..X'],['XXX']],
    '4': [['X.X'],['X.X'],['XXX'],['..X'],['..X']],
    '5': [['XXX'],['X..'],['XXX'],['..X'],['XXX']],
    '6': [['XXX'],['X..'],['XXX'],['X.X'],['XXX']],
    '7': [['XXX'],['..X'],['..X'],['..X'],['..X']],
    '8': [['XXX'],['X.X'],['XXX'],['X.X'],['XXX']],
    '9': [['XXX'],['X.X'],['XXX'],['..X'],['XXX']],
    ' ': [['.'],['.'],['.'],['.'],['.']],
}
num_list = [i for i in num_str]
num_str = ' '.join(num_list)
# print(num_str)
for i in range(len(num_dic['0'])):
    for j in num_str:
        print(num_dic[j][i][0],end='')
    print('')