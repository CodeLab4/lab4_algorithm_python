def solution(clothes):
    answer = 0

    dic = dict({item[1]: [] for item in clothes})
    for i in clothes:
        dic[i[1]].append(i[0])

    count = 1
    for j in dic:
        count *= len(dic[j]) + 1
    answer = count - 1

    return answer
