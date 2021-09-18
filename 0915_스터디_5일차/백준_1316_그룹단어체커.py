import sys
sys.stdin = open('input_1316.txt', 'r')

TC = int(input())
result_cnt = 0
for test_case in range(1, TC+1):
    word = input()
    exist_list = [] # 이미 있는 알파벳을 넣는 리스트
    cnt = 0

    for i in word: # 단어에서 한글자씩 꺼내서 비교해보기
        if i not in exist_list:
            exist_list.append(i)
        elif i in exist_list: # 이미 있는 리스트에 있는데
            if exist_list[-1] == i: # 그 리스트의 맨끝에 위치하면 패스
                continue
            else: # 그 리스트의 맨끝이 아닌 위치에 있으면 그룹단어가 아니므로 cnt를 늘린다.
                cnt +=1
                break # 그룹단어 아닌걸 알았으니 브레이크 걸어주기
    result_cnt += cnt # cnt가 단어마다 리셋되므로 result_cnt에 담아준다.

print(TC - result_cnt) # 전체 경우에서 그룹단어 아닌경우를 빼면 그룹단어인 경우가 된다.
