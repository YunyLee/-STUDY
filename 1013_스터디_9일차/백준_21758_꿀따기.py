import sys
sys.stdin = open('input_21758.txt', 'r')

TC = int(input())

for test_case in range(1, TC+1):
    N = int(input()) # 장소의 수
    HONEY = list(map(int,input().split()))
    max_honey = 0



    print(max_honey)