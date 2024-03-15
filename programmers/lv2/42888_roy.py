from collections import defaultdict


def solution(record):
    answer = []

    nick_dic = defaultdict(str)
    status_lst = []

    for m in record:
        temp = m.split()
        status_lst.append((temp[0], temp[1]))

        if len(temp) == 3:
            nick_dic[temp[1]] = (temp[2])

    for sl in status_lst:

        if sl[0] == 'Enter':
            message = nick_dic[sl[1]] + '님이 ' + '들어왔습니다.'
            answer.append(message)
        elif sl[0] == 'Leave':
            message = nick_dic[sl[1]] + '님이 ' + '나갔습니다.'
            answer.append(message)

    return answer
