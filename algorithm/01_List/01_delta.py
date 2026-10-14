"""
5×5 이차원 배열(matrix)의 모든 원소를 하나씩 확인하면서,
각 원소를 기준으로 상하좌우에 어떤 값이 있는지 탐색하는 코드
"""

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = 5
mat = [
    [1,  2,  3,  4,  5],
    [6,  7,  8,  9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

for row in range(n):
    for col in range(n):
        for k in range(4):
            nx = row + dx[k] # 좌표값
            ny = col + dy[k] # 좌표값

            if 0 <= nx < n and 0 <= ny < n:
                print('row, col에 대하여', mat[row][col])
                print(dx[k], dy[k])
                print(mat[nx][ny])