_dic = {
    'a':'+',
    'b':'-',
    'c':'*'
}

num = int(input().strip())
tem_sign = ''
for i in range(num):
    equation_list = input().split()
    # print(equation_list)
    if len(equation_list) == 3:
        equation_list[1] = int(equation_list[1])
        equation_list[2] = int(equation_list[2])
        tem_sign = equation_list[0]
        if equation_list[0] == 'a':
            tem_ans = equation_list[1] + equation_list[2]
        elif equation_list[0] == 'b':
            tem_ans = equation_list[1] - equation_list[2]
        elif equation_list[0] == 'c':
            tem_ans = equation_list[1] * equation_list[2]
        ans_str = f'{equation_list[1]}{_dic[equation_list[0]]}{equation_list[2]}={tem_ans}'
        print(ans_str)
        print(len(ans_str))
    else:
        equation_list[0] = int(equation_list[0])
        equation_list[1] = int(equation_list[1])
        if tem_sign == 'a':
            tem_ans = equation_list[0] + equation_list[1]
        elif tem_sign == 'b':
            tem_ans = equation_list[0] - equation_list[1]
        elif tem_sign == 'c':
            tem_ans = equation_list[0] * equation_list[1]
        ans_str = f'{equation_list[0]}{_dic[tem_sign]}{equation_list[1]}={tem_ans}'
        print(ans_str)
        print(len(ans_str))
