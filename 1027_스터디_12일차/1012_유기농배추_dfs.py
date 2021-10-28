import sys
sys.stdin = open('input_1012.txt', 'r')
sys.setrecursionlimit()
def find_cabbage(row, col):

    # 정지조건 - 가지치기
    if row<0 or row>=N or col<0 or col>=M: # 기본인덱스 범위를 벗어나면
        return

    if not ARR[row][col]: # 배추가 없으면
        return

    ARR[row][col] = 0  # 지나간곳은 0으로 표시해주기

    find_cabbage(row, col+1)  # 우
    find_cabbage(row+1, col)  # 하
    find_cabbage(row, col-1)  # 좌
    find_cabbage(row-1, col)  # 상

TC = int(input())
for test_case in range(1, TC+1):
    N, M, K = map(int,input().split())
    ARR = [[0]*M for _ in range(N)] # M은 가로 N은 세로

    for k in range(K):
        a, b = map(int,input().split())
        ARR[a][b] = 1 # ARR배열에 배추 표시해주기

    cnt = 0
    for i in range(N):
        for j in range(M):
            if ARR[i][j]:
                cnt += 1
                find_cabbage(i, j)

    print(cnt)