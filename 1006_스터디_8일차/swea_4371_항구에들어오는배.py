import sys
sys.stdin = open('input_4371.txt', 'r')

#  항구에 들어오는 배

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input()) # 즐거운 날의 수
    result = 0
    information_list = []
    for i in range(N):
        INFORMATION = int(input()) # 즐거운 날의 정보
        information_list.append(INFORMATION)

    information_list.pop(0) # 첫번째 인덱스 지워주기 -
                            # 이유 : 어차피 첫번째날과의 차이만큼씩 빼줄거라서 항상 0이기 때문

    diff_list = []
    for i in information_list:
        diff_list.append(i-1) # 1은 첫번째날과의 차이를 의미 / 그 차이들을 담은 diff_list 만들기
                              # 2번째 테스트 케이스를 기준으로 [6, 9, 12, 18]이 만들어진다.

    result_set = set(diff_list) # 리스트끼리 뺄 수 없으므로 set으로 변환
    for i in diff_list:
        if i in result_set and len(result_set) != 0:
            result_set -= set(range(i, diff_list[-1]+1, i))
            result += 1

    print('#{} {}'.format(test_case, result))