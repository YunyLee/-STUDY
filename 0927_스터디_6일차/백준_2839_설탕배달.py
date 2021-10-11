import sys
sys.stdin = open('input_2839.txt', 'r')

# 백준 2839 브론즈1 설탕배달

TC = int(input())

for test_case in range(1, TC+1):
    SUGAR = int(input())

    cnt = 0

    while SUGAR >= 0:
        if SUGAR == 1 or SUGAR == 2:
            cnt = -1
            break
        if SUGAR % 5 == 0:
            cnt += SUGAR//5
            break
        else:
            SUGAR -= 3
            cnt += 1

    print(cnt)