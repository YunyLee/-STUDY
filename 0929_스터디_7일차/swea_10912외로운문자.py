import sys
sys.stdin = open('input_10912.txt', 'r')

TC = int(input())

for test_case in range(1, TC+1):
    WORD = list(map(str,input()))
    result = []
    final_result = ''

    for i in WORD:
        if i not in result: # 비교할 단어를 하나 꺼내주고
            result.append(i)
        elif i in result: # 해당 단어가 있었으면 지워주고
            result.remove(i)

    result.sort() # 리스트인 상태에서 순서 정렬
    for i in result: # string형태로 만들어주기
        final_result += i

    if len(result) == 0:
        final_result = 'Good'

    print('#{} {}'.format(test_case, final_result))