def solution(n):
    answer = 0

    for i in range(1, n + 1):  # 1~15
        sum = 0
        num = i
        while sum < n:
            sum += num
            if sum == n:
                answer += 1
            num += 1

    return answer
