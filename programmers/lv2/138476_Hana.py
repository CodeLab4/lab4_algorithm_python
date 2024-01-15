from collections import Counter


def solution(k, tangerine):
    answer = 0

    counter = Counter(tangerine)
    sorted_lst = sorted(counter.values(), reverse=True)

    i = 0
    t = 0  # 포장한 귤의 개수

    while t < k:
        t += sorted_lst[i]
        answer += 1
        i += 1

    return answer
