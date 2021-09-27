import sys
sys.stdin = open('input_6019.txt', 'r')

TC = int(input())

for test_case in range(1, TC+1):
    D, A, B, F = map(int,input().split())
    result = 0
    # 거리 = 속력 * 시간
    # D = (A+B) * time
    # 두 기차사이의 거리 250 = (A속력 + B속력) * 시간
    # 그런데 미지수 설정을 할 수 없으므로 time = 으로 정리할 수 있게 뒤로 보내준다.

    time = D / (A+B)

    # 파리가 이동한 거리 = 파리의 속력 * 시간
    # 그런데 파리가 이동한 시간은 기차가 부딪히는 시간과 같으므로 위에서 구한 time활용

    result = F * time

    print('#{} {}'.format(test_case, result))