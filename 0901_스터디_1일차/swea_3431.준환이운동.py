import sys
sys.stdin = open('input_3431.txt', 'r')

# swea 3431 준환이의 운동관리

TC = int(input())

for test_case in range(1, TC+1):
    MIN_MINUTE, MAX_MINUTE, EXERCISE = map(int,input().split())

    result = 0

    # 1. 준환이가 알맞은시간 운동한 경우 : 추가시간 0 반환
    if MIN_MINUTE <= EXERCISE <= MAX_MINUTE:
        result = 0
    # 2. 준환이가 초과해서 운동한 경우 : -1 반환
    elif EXERCISE > MAX_MINUTE:
        result = -1
    # 3. 준환이가 덜 운동한 경우 : 추가로 해야하는 운동시간 반환
    else:
        result = (MIN_MINUTE - EXERCISE)

    print('#{} {}'.format(test_case, result))