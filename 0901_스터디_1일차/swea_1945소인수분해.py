import sys
sys.stdin = open('input_1945.txt', 'r')

# swea 1945 소인수분해

TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())

    # N에서 2, 3, 5, 7, 11이 몇개씩 있는지 count하는 문제

    sosu = [2, 3, 5, 7, 11]
    cnt_list = [0] * 5 # 위의 소수를 count해줄 빈 리스트 생성

    for i in range(len(sosu)):
        # 처음에는 N과 같은 값인 process_N을 소수의 0번째 값인 2로 나눴을때 나머지가 0이라면 (딱 떨어진다는것)
        while N % sosu[i] == 0:
            N = N/sosu[i] # N을 0번째값인 소수 2로 나눈값을 다시 N에 저장해준다.(무한루프 돌지 않기위해)
            cnt_list[i] += 1 # 0번째 값인 소수 2로 나누는 과정을 1번 했다고 0번째 카운트 리스트에 1증가

    result = '' # 리스트 괄호 빼고 해주는 작업 .join()으로 하고싶지만 이건 str만 가능하다.
    for i in cnt_list:
        result += str(i) + ' '

    print('#{} {}'.format(test_case, result))