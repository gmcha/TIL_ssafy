from collections import deque

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 각 방향의 반대 방향
opposite = [1, 0, 3, 2]

# 터널 종류별 이동 가능한 방향
tunnel = [
    [],             # 0번: 터널 없음
    [0, 1, 2, 3],   # 1번: 상하좌우
    [0, 1],         # 2번: 상하
    [2, 3],         # 3번: 좌우
    [0, 3],         # 4번: 상우
    [1, 3],         # 5번: 하우
    [1, 2],         # 6번: 하좌
    [0, 2]          # 7번: 상좌
]


def bfs(sr, sc):
    q = deque()
    visited = [[0] * M for _ in range(N)]

    # 시작 위치 초기화
    q.append((sr, sc))
    visited[sr][sc] = 1
    cnt = 1

    while q:
        r, c = q.popleft()

        # 제한 시간에 도달하면 더 이상 이동하지 않음
        if visited[r][c] == L:
            continue

        # 현재 터널에서 이동 가능한 방향만 탐색
        for d in tunnel[arr[r][c]]:
            nr = r + dr[d]
            nc = c + dc[d]

            # 1. 배열 범위 검사
            if not (0 <= nr < N and 0 <= nc < M):
                continue

            # 2. 방문 여부 검사
            if visited[nr][nc] != 0:
                continue

            # 3. 터널 존재 여부 검사
            if arr[nr][nc] == 0:
                continue

            # 4. 다음 터널과 연결되어 있는지 검사
            if opposite[d] not in tunnel[arr[nr][nc]]:
                continue

            # 모든 조건을 만족하면 방문 처리
            visited[nr][nc] = visited[r][c] + 1
            q.append((nr, nc))
            cnt += 1

    return cnt


T = int(input())

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = bfs(R, C)

    print(f'#{tc} {ans}')