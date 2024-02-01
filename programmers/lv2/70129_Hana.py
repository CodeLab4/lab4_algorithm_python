def solution(s):
    answer = []

    delete_cnt = 0
    convert_cnt = 0

    while (True):
        delete_cnt += s.count('0')
        s = bin(s.count('1'))[2:]
        convert_cnt += 1

        if s == '1':
            break

    answer = [convert_cnt, delete_cnt]

    return answer
