from collections import deque


def solution(land):
    answer = 0
    n, m = len(land), len(land[0])
    visited = [[False] * m for _ in range(n)]
    oil = [0] * m
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    def bfs(row, col):
        queue = deque()
        queue.append([row, col])
        visited[row][col] = True
        cnt = 1
        oil_covered = {col}

        while queue:
            pr, pc = queue.popleft()
            for dr, dc in directions:
                nr, nc = pr + dr, pc + dc
                if 0 <= nr < n and 0 <= nc < m and land[nr][nc] == 1 and not visited[nr][nc]:
                    queue.append([nr, nc])
                    visited[nr][nc] = True
                    cnt += 1
                    oil_covered.add(nc)

        for c in oil_covered:
            oil[c] += cnt

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                bfs(i, j)

    answer = max(oil)

    return answer
