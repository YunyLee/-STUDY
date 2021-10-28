import sys
sys.stdin = open('input_5431.txt', 'r')

TC = int(input())

for test_case in range(1, TC+1):
    N, K = map(int, input().split())
    ARR = list(map(str,input().split()))
    temp = []

    for i in range(1, N+1):
        temp.append(str(i))

    for i in ARR:
        if i in temp:
            temp.remove(i)

    print('#{} {}'.format(test_case, ' '.join(temp)))