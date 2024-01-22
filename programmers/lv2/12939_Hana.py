def solution(s):
    answer = ''

    lst = [int(i) for i in s.split(' ')]
    answer = str(min(lst)) + ' ' + str(max(lst))

    return answer
