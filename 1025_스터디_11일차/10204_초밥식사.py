import sys
sys.stdin = open('input_10204.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input()) # 접시의 수
    jeongyeon_list = []
    hyeonyong_list = []
    for i in range(N):
        a, b = map(int,input().split())
        jeongyeon_list.append(a)
        hyeonyong_list.append(b)
    happiness_jeongyeon = happiness_hyeonyong = 0

    # 1순위 : 내 행복도가 가장 높은것
    # 2순위 : 상대방의 행복도가 가장 높은것

    for i in range(1, N+1):
        # 홀수번째 순서는 정연이가 먹을 차례
        if i%2:
            if jeongyeon_list.count(max(jeongyeon_list)) > 1: # 2개 이상이면
                temp_idx = hyeonyong_list.index(max(hyeonyong_list))
                hyeonyong_list.pop(temp_idx)
                happiness_jeongyeon += jeongyeon_list.pop(temp_idx)
            else: # 최대행복도가 1개이면
                temp_idx = jeongyeon_list.index(max(jeongyeon_list))
                happiness_jeongyeon += jeongyeon_list.pop(temp_idx)
                hyeonyong_list.pop(temp_idx)
        # 짝수번째 순서는 현용이가 먹을 차례
        else:
            if hyeonyong_list.count(max(hyeonyong_list)) > 1:  # 2개 이상이면
                temp_idx = jeongyeon_list.index(max(jeongyeon_list))
                jeongyeon_list.pop(temp_idx)
                happiness_hyeonyong += hyeonyong_list.pop(temp_idx)
            else:  # 최대행복도가 1개이면
                temp_idx = hyeonyong_list.index(max(hyeonyong_list))
                happiness_hyeonyong += hyeonyong_list.pop(temp_idx)
                jeongyeon_list.pop(temp_idx)

    result = happiness_jeongyeon - happiness_hyeonyong  # 정연이의 행복도 - 현용이의 행복도

    print(f'#{test_case} {result}')
