import sys
sys.stdin = open('input_2817.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    N, K = map(int,input().split())
    # 마치 딕셔너리처럼 만들기
    ARR_key = list(range(N))
    ARR_value = list(map(int,input().split()))
    cnt = 0

    for i in ARR_key: # 인덱스 뽑아내려구
        for j in range(i+1, N):
            for k in range(j+1, N):
                # 1개일때
                if ARR_value[i] == K:
                    cnt += 1
                # 2개일때
                if ARR_value[i]+ARR_value[j] == K:
                    cnt += 1
                # 3개일때
                if ARR_value[i]+ARR_value[j]+ARR_value[k] == K:
                    cnt += 1

    print(f'#{test_case} {cnt}')
