import sys
sys.stdin = open('input_2805.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    benefit = 0
    for i in range(N):
        mid = N // 2
        if i <= mid:
            for j in range(mid-i, mid+i+1):
                benefit += farm[i][j]
        else:
            for j in range(mid+(i-mid), mid-(i-mid)+1, -1):
                benefit += farm[i][j]
    print(f'#{tc} {benefit}')