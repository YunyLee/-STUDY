import sys
sys.stdin = open('input_1946.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    wrd = ''
    for z in range(N):
        Ci, Ki = map(str, input().split())
        wrd += Ci*int(Ki)
    print(f'#{tc}')
    for w in range(len(wrd)):
        if (w+1) % 10 == 0:
            print(wrd[w])
        else:
            print(wrd[w], end='')