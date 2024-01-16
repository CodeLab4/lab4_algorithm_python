def solution(citations):
    answer = 0

    citations.sort()
    result = []

    for h in range(len(citations) + 1):
        more = sum(1 for item in citations if h <= item)
        if more >= h:
            result.append(h)

    answer = max(result, default=0)

    return answer
