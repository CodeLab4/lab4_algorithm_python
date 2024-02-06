def dfs(sum, target, numbers, v):
    global answer

    if v == len(numbers):
        if sum == target:
            answer += 1
            print(sum)
        return

    dfs(sum + numbers[v], target, numbers, v + 1)
    dfs(sum - numbers[v], target, numbers, v + 1)


def solution(numbers, target):
    global answer
    answer = 0

    dfs(0, target, numbers, 0)

    return answer
