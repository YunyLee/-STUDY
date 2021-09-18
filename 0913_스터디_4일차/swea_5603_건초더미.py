import sys
sys.stdin = open('input_5603.txt', 'r')

# swea 5603 건초더미

TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    s = []
    cnt = 0
    for i in range(N):
        s.append(int(input()))

    average_num = int(sum(s)/len(s)) # 평균값을 구해주고
    for i in s:
        cnt += abs(average_num-i) # 절대값 만큼 카운트해서

    print('#{} {}'.format(test_case, int(cnt/2))) # 그값을 2로 나누기