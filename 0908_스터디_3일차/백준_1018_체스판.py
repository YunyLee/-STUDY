import sys
sys.stdin = open('input_1018.txt', 'r')

N, M = map(int, input().split())
BRD = [list(map(str, input())) for _ in range(N)]
black_first = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
white_first = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
min_cnt = 1000000000

for row in range(N-8+1):
    for col in range(M-8+1):
        cnt = 0
        # if BRD[row][col] == 'B' or BRD[row][col] == 'W':
            white_cnt:
            black_cnt = 0
            for i in range(row, row+8, 2):
                for j in range(0, 8):
                    if white_first[j] != BRD[i][col+j]:
                        white_cnt += 1
            for i in range(row+1, row+8, 2):
                for j in range(0, 8):
                    if black_first[j] != BRD[i][col+j]:
                        white_cnt += 1
            for i in range(row, row+8, 2):
                for j in range(0, 8):
                    if black_first[j] != BRD[i][col+j]:
                        black_cnt += 1
            for i in range(row+1, row+8, 2):
                for j in range(0, 8):
                    if white_first[j] != BRD[i][col+j]:
                        black_cnt += 1
            if black_cnt >= white_cnt:
                cnt = white_cnt
            else:
                cnt = black_cnt
        if min_cnt > cnt:
            min_cnt = cnt

print(min_cnt)

# for row in range(N):
#     min_cnt = 0 # 여기가 초기화인 이유는 줄마다 계산하기 때문
#     cnt = 0
#     for col in range(N-M+1): # 0, 1, 2, 3
#         for i in range(col,M-col):
#             if BRD[row][i] == 'W':
#                 for j in range(i+1,M,2): #홀수씩
#                     if BRD[row][j] != 'B': # 0번째줄의 [1][3][5][7]..
#                         cnt += 1
#                     if BRD[row][j-1] != 'W':  # 0번째줄의 [0][2][4][6]..
#                         cnt += 1
#             if BRD[row][i] == 'B':
#                 for j in range(i+1,M,2): #홀수씩
#                     if BRD[row][j] != 'W': # 0번째줄의 [1][3][5][7]..
#                         cnt += 1
#                     if BRD[row][j-1] != 'B':  # 0번째줄의 [0][2][4][6]..
#                         cnt += 1
#             if min_cnt > cnt:
#                 min_cnt = cnt
#     result += min_cnt
#
# print(min_cnt)


# M, N = map(int,input().split())
# BRD = [list(map(str,input())) for _ in range(M)]
#
# cnt = 0
#
# for i in range(0,M):
#     if BRD[i][0] == 'W':
#         for j in range(1,N,2): #홀수씩
#             if BRD[i][j] != 'B': # 0번째줄의 [1][3][5][7]..
#                 cnt += 1
#             if BRD[i][j-1] != 'W':  # 0번째줄의 [0][2][4][6]..
#                 cnt += 1
#     if BRD[i][0] == 'B':
#         for j in range(1,N,2): #홀수씩
#             if BRD[i][j] != 'W': # 0번째줄의 [1][3][5][7]..
#                 cnt += 1
#             if BRD[i][j-1] != 'B':  # 0번째줄의 [0][2][4][6]..
#                 cnt += 1
#
# print(cnt)