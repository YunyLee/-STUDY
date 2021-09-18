import sys
sys.stdin = open('input_4299.txt', 'r')

# swea d2 4299 태혁이의 사랑은 타이밍

# 태혁이가 바람을 맞으며 기다린 시간을 계산하자

# 깨달음을 얻은시간 D일 H시 M분

TC = int(input())

for test_case in range(1, TC+1):
    D, H, M = map(int, input().split())

    result = 0

    minus_date = 0
    minus_date_time = 0
    minus_hour = 0
    minus_hour_time = 0
    minus_minute_time = 0

    # 큰틀 3가지 D > 11 경우와  D == 1 경우와 D < 11경우를 정의해서
    # 그 아래에 각각 H경우와 M경우를 생각해서 이어가는 식으로 풀기!

    if D>11:
        minus_date = D-11
        minus_date_time = (minus_date * 24 * 60)

        if H <11:
            minus_hour = 24 - (11-H)
            minus_date_time -= 60*24
            minus_hour_time = minus_hour * 60
            if M < 11:
                minus_minute_time = 60 - (11 - M)
                minus_hour_time -= 60
            elif M == 11:
                minus_minute_time = 0
            elif M > 11:
                minus_minute_time = M - 11
        elif H == 11:
            minus_hour_time = 0
            if M < 11:
                minus_minute_time = 60 - (11 - M)
                minus_hour_time -= 60
            elif M == 11:
                minus_minute_time = 0
            elif M > 11:
                minus_minute_time = M - 11
        else: # H > 11
            minus_hour = H-11
            minus_hour_time = minus_hour * 60
            if M < 11:
                minus_minute_time = 60 - (11 - M)
                minus_hour_time -= 60
            elif M == 11:
                minus_minute_time = 0
            elif M > 11:
                minus_minute_time = M - 11

    elif D==11:
        minus_date_time = 0

        # Day가 같은데 H가 더 작으면 약속시간전에 차인것
        if H<11:
            result = -1
        elif H==11:
            minus_hour_time = 0
            # D == 11 이고 H == 11인 상태에서 M을 볼 차례
            if M < 11:
                result = -1
            elif M == 11:
                minus_minute_time = 0
            elif M > 11:
                minus_minute_time = M-11
        else: #H>11
            minus_hour = H-11
            minus_hour_time = (minus_hour * 60)
            # D = 11 이고 H > 11 인 상테에서 이제 M을 볼 차례
            if M < 11:
                minus_minute_time = 60 - (11 - M)
                minus_hour_time -= 60
            elif M == 11:
                minus_minute_time = 0
            elif M > 11:
                minus_minute_time = M-11

    else: # D<11
        result = -1

    if result != -1:
        result = minus_date_time + minus_hour_time + minus_minute_time

    print('#{} {}'.format(test_case, result))