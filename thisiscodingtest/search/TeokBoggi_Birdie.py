counts, teok_length = map(int, input().split())

teok_list = list(map(int, input().split()))

answer = 0

start = 0
end = max(teok_list)

while start <= end:
    total = 0
    mid = (start + end) // 2

    for x in teok_list:
        if x > mid:
            total += x - mid

    if total < teok_length:
        end = mid - 1

    else:
        answer = mid
        start = mid + 1

print(answer)
