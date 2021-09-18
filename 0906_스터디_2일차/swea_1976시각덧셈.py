import sys
sys.stdin = open('input_1976.txt', 'r')

# swea d2 1976 시각덧셈

TC = int(input())

for test_case in range(1, TC+1):
    H1, M1, H2, M2 = map(int,input().split())

    result_h = 0
    result_m = 0

    if H1 + H2 <=12:
        result_h = H1 + H2
    elif H1 + H2 >=13:
        result_h = (H1 + H2) - 12

    if M1 + M2 <= 59:
        result_m = M1 + M2
    elif M1 + M2 >= 60:
        result_m = (M1 + M2) - 60
        result_h += 1

    print('#{} {} {}'.format(test_case, result_h, result_m))