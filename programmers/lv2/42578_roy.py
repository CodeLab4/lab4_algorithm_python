def solution(clothes):
    dic = {}

    for i in clothes:
        if i[1] in dic:
            dic[i[1]] += 1
        else:
            dic[i[1]] = 1

    answer = 1
    for i in dic.values():
        answer *= (i + 1)

    return answer - 1
