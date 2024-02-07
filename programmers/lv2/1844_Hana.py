from collections import deque


def bfs(maps, start_row, start_col, visited):
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    queue = deque([(start_row, start_col)])
    visited[start_row][start_col] = 1

    while queue:
        row, col = queue.popleft()
        for dr, dc in direction:
            nr, nc = row + dr, col + dc
            if 0 <= nr < len(maps) and 0 <= nc < len(maps[0]) and visited[nr][nc] == -1 and maps[nr][nc] == 1:
                queue.append((nr, nc))
                visited[nr][nc] = visited[row][col] + 1


def solution(maps):
    visited = [[-1 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    bfs(maps, 0, 0, visited)
    print(visited)

    return visited[len(maps) - 1][len(maps[0]) - 1]
