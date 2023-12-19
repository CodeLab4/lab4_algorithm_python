import re

def solution(dartResult):
    answer = 0

    result_lst = re.split(r'([SDT*#])', dartResult)
    calculate_dic = {'S': '**1', 'D': '**2', 'T': '**3'}

    score_lst = list()
    for index, value in enumerate(result_lst):
        if index % 2 != 0 and value in calculate_dic:
            expression = result_lst[index - 1] + calculate_dic[value]
            score_lst.append(eval(expression))
        elif value == '*':
            if len(score_lst) > 1:
                score_lst[-2] *= 2
            score_lst[-1] *= 2
        elif value == '#':
            score_lst[-1] *= -1

    answer = sum(score_lst)

    return answer
