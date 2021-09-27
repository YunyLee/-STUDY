import sys
sys.stdin = open('input_12927.txt', 'r')

TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    LIGHT_LIST = list(map(str,input()))

    origin = ['N'] * N
    cnt = 0

    for i in range(1, N+1):
        if LIGHT_LIST[i-1] != origin[i-1]:
            for j in range(i-1, N, i):
                if LIGHT_LIST[j] == 'Y':
                    LIGHT_LIST[j] = 'N'
                elif LIGHT_LIST[j] == 'N':
                    LIGHT_LIST[j] = 'Y'
            cnt += 1
        elif LIGHT_LIST == origin:
            break
    print(cnt)