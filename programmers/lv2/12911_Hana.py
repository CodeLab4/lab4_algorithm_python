def solution(n):
    answer = 0

    for i in range(n + 1, 1000000):
        if str(format(n, 'b')).count('1') == str(format(i, 'b')).count('1'):
            answer = i
            break

    return answer
