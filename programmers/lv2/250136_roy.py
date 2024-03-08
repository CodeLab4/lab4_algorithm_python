from collections import deque


def solution(land):
    answer = 0

    n, m = len(land), len(land[0])
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    result = []
    for i in range(m):
        visited = [[False] * m for _ in range(n)]
        cnt = 0
        for j in range(n):
            if land[j][i] == 1 and not visited[j][i]:
                queue = deque()
                queue.append((j, i))
                visited[j][i] = True
                cnt += 1

                while queue:
                    row, col = queue.popleft()
                    for dr, dc in directions:
                        nr = row + dr
                        nc = col + dc
                        if 0 <= nr < n and 0 <= nc < m and land[nr][nc] == 1 and not visited[nr][nc]:
                            queue.append((nr, nc))
                            visited[nr][nc] = True
                            cnt += 1

        result.append(cnt)

    answer = max(result)
    return answer
