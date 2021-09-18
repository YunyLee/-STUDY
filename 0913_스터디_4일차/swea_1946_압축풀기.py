import sys
sys.stdin = open('input_1946.txt', 'r')

# swea 1946 간단한 압축풀기

TC = int(input())

for test_case in range(1, TC+1):
    ALPHA_CNT = int(input())
    document = '' # 일단 초기화하고 다 담아준다.
    for i in range(ALPHA_CNT):
        ALPHABET, NUM = list(map(str,input().split()))
        document += ALPHABET * int(NUM)

    print('#{}'.format(test_case))
    for i in range(len(document)):
        if (i+1) % 10 != 0:
            print(document[i], end='')
        else:
            print(document[i])
    print()


