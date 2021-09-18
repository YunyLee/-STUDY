import sys
sys.stdin = open('input_1204.txt', 'r')

# swea 1204 최빈수 구하기

TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    SCORE_LIST = list(map(int, input().split()))

    blank_list = [0] * 101 # 0점부터 100점까지 빈 성적 리스트

    for i in SCORE_LIST: # 점수를 순서대로 하나씩 뽑는다.
        blank_list[i] += 1 # 점수에 해당하는 위치에 카운트 1개씩 증가시킨다.
        # ex) 71점이면 blank_list의 71번째 인덱스 자리에 카운트 1을 증가

    max_cnt = max(blank_list) # 제일 높은 카운트 수를 찾는다. 그게 제일 자주 나온 점수니까
    for i in range(len(blank_list)): # blank_list에서 인덱스를 하나씩 뽑아내서
        if blank_list[i] == max_cnt: # 예를 들어 71번째 인덱스에 17이라는 값이 저장되어있는데, max_cnt와도 같다면
            result = i # 최빈값은 17번 등장한 71이 된다. 그래서 그 인덱스인 i를 저장하는 것!

    print('#{} {}'.format(N, result))