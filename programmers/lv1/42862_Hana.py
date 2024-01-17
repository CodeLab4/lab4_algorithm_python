def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()

    to_remove = [i for i in lost if i in reserve]
    lost = [i for i in lost if i not in to_remove]
    reserve = [i for i in reserve if i not in to_remove]

    to_remove = list()
    for i in lost:
        if i - 1 in reserve:
            to_remove.append(i)
            reserve.remove(i - 1)
        elif i + 1 in reserve:
            to_remove.append(i)
            reserve.remove(i + 1)

    lost = [i for i in lost if i not in to_remove]
    answer = n - len(lost)

    return answer
