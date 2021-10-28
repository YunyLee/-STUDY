import sys
sys.stdin = open('input_11586.txt', 'r')

N = int(input()) # 마법거울의 크기
mirror = [list(map(str,input())) for _ in range(N)]
status = int(input())

# status가 1일때, 공주님 모습 그대로
# 2일때, 좌/우 반전
# 3일때 상/하 반전

if status == 1:
    for i in range(N):
        print(''.join(mirror[i]))
elif status == 2:
    for i in range(N):
        print(''.join(mirror[i][::-1]))
else:
    for i in range(N-1, -1, -1):
        print(''.join(mirror[i]))