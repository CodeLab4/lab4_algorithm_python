def solution(citations):
    answer = 0

    citations.sort(reverse=True)

    h = len(citations)
    flag = False

    while not flag:
        cnt = 0
        for i in citations:
            if i >= h:
                cnt += 1
        if cnt >= h:
            flag = True
            answer = h
        h -= 1

    return answer
