import sys
sys.stdin = open('input_1012.txt', 'r')

def find_cabbage(row, col):
    global cnt

    # 우하좌상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    direction = 0 # 오른쪽부터 시작

    while True:
        ARR[row][col] = 0

        row += dr[direction]
        col += dc[direction]
        # 만약에 기본 인덱스 범위 안에 있고, 지금 좌표에 값이 있으면
        if 0<=row<N and 0<=col<M and ARR[row][col]:
            continue
        else:
            row -= dr[direction]
            col -= dc[direction]

            direction = (direction + 1) % 4

        if 0<= row-1 <N and 0<=row+1<N and 0<=col-1<N and 0<=col+1<N:
            if not ARR[row-1][col] and not ARR[row+1][col] and not ARR[row][col-1] and not ARR[row][col+1]:
                return

TC = int(input())
for test_case in range(1, TC+1):
    N, M, K = map(int,input().split())
    ARR = [[0]*M for _ in range(N)] # 가로 M 세로 N
    for k in range(K):
        x, y = map(int, input().split())
        ARR[x][y] = 1
    cnt = 0

    for i in range(N): # row
        for j in range(M): # col
            if ARR[i][j]:
                cnt += 1
                find_cabbage(i, j)

    print(f'#{test_case} {cnt}')


