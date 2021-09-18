import sys
sys.stdin = open('input_2805.txt', 'r')

TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    FARM = [list(map(int,input())) for _ in range(N)]
    result = 0

    half = int(N/2)
    first_num = 0 # 첫번째 인덱스
    last_num = N # 마지막 인덱스
    uphalf = half # 가운데에서 위로 줄어드는 인덱스
    downhalf = half # 가운데에서 아래로 늘어나는 인덱스
    result += sum(FARM[half][first_num:N]) # 가운데 인덱스값 합계

    while uphalf !=0 and downhalf != N-1:
        first_num += 1
        last_num -= 1
        uphalf -= 1
        downhalf += 1
        result += sum(FARM[uphalf][first_num:last_num])
        result += sum(FARM[downhalf][first_num:last_num])

    print('#{} {}'.format(test_case, result))