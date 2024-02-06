def solution(numbers, target):
    answer = dfs_counter(numbers, target, 0, 0)

    return answer


def dfs_counter(numbers, target, num_sum, depth):
    cnt = 0

    def dfs(numbers, target, num_sum, depth):
        nonlocal cnt
        if depth == len(numbers):
            if num_sum == target:
                cnt += 1
            return

        dfs(numbers, target, num_sum + numbers[depth], depth + 1)
        dfs(numbers, target, num_sum - numbers[depth], depth + 1)

    dfs(numbers, target, num_sum, depth)
    return cnt
