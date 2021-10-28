import sys
sys.stdin = open('input_5601.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    result = ('1/' + str(N) + ' ')*int(N)
    print(f'#{test_case}', result)