import sys
sys.stdin = open('input_1012.txt', 'r')

# 행렬로 풀려고 했음.
# 아무래도 dfs 활용해야 될 것 같다.

def find_cabbage():
    global cnt

    for i in range(N+2):
        for j in range(M+2):
            if arr[i][j] and not arr[i-1][j] and not arr[i][j-1]:
                cnt += 1

TC = int(input())
for test_case in range(1, TC+1):
    N, M, K = map(int,input().split())
    arr = [[0]*M for _ in range(N)]
    for m in range(K):
        a, b = map(int,input().split())
        arr[a][b] = 1

    # 우선 좌표에 맞게 1표시를 다 해준 후, 갑옷을 입힌다.
    for lst in arr:
        lst.insert(0, 0)
        lst.append(0)
    arr.append([0]*(M+2))
    arr.insert(0, [0]*(M+2))
    # 갑옷 두르기 완성

    cnt = 0
    find_cabbage()
    print(cnt)


