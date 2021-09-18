import sys
sys.stdin = open('input_1984.txt', 'r')

# swea 1984 중간평균값

TC = int(input())

for test_case in range(1, TC+1):

    NUM_LIST = list(map(int,input().split()))
    result = 0

    NUM_LIST.remove(max(NUM_LIST))
    NUM_LIST.remove(min(NUM_LIST))

    result = sum(NUM_LIST)/(len(NUM_LIST))
    result = round(result)

    print('#{} {}'.format(test_case, int(result)))