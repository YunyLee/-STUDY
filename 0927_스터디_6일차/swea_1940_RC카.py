import sys
sys.stdin = open('input_1940.txt', 'r')

# 가랏! RC카!

TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    result = 0
    for i in range(N):
        if input() != 0:
            TIME, SPEED = map(int,input().split())
        else:
            SPEED = int(input())
    print(TIME, SPEED)
    print('#{} {}'.format(test_case, result))