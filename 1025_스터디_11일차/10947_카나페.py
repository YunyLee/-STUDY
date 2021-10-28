import sys
sys.stdin = open('input_10947.txt')

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    biscuit = list(map(int,input().split()))
    flavor = list(map(int,input().split()))

    biscuit_copy = biscuit
    flavor_copy = flavor
    best_canape = 0

    for i in range(N):
        temp_biscuit = biscuit_copy.pop(biscuit_copy.index(max(biscuit_copy)))
        temp_flavor = flavor_copy.pop(flavor_copy.index(max(flavor_copy)))
        best_canape += temp_biscuit * temp_flavor

    print(f'#{test_case} {best_canape}')