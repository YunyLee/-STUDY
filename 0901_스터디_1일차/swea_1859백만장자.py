import sys
sys.stdin = open('input_practice.txt', 'r')

# swea 1859 백만장자 프로젝트

TC = int(input())

for test_case in range(1, TC + 1):
    N = int(input())
    N_LIST = list(map(int, input().split()))

    max_price = N_LIST[-1]  # 리스트의 가장 마지막값을 max_price로 넣어주자
    result = 0

    # 뒤에서부터 시세차익만큼 누적하자
    for i in range(N - 2, -1, -1):  # N-1이 이미 max_price니까 비교할 이유가 없다.
        if max_price > N_LIST[i]:  # i번째 값이 최대값보다 작다면, 시세차익 더해주기
            result += max_price - N_LIST[i]
        else:  # 최대값보다 크면 최대값을 대체하자
            max_price = N_LIST[i]

    print('#{} {}'.format(test_case, result))
