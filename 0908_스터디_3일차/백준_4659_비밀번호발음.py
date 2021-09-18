import sys
sys.stdin = open('input_4659.txt', 'r')

# 백준 4659 비밀번호 발음
vowel = ['a','e','i','o','u']

while True :
    WORD = input()
    # end가 오면 break하기
    if WORD == 'end':
        break
    result = 'not acceptable.'
    # 모음이 있으면 acceptable 출력하기
    for i in vowel:
        if i in WORD:
            result = 'acceptable.'

    # 모음 or 자음 3글자 이상 연속으로 오면 안 된다.
    if len(WORD) >= 3:
        for i in range(len(WORD)-2):
            if WORD[i] in vowel and WORD[i+1] in vowel and WORD[i+2] in vowel:
                result = 'not acceptable.'
            if WORD[i] not in vowel and WORD[i+1] not in vowel and WORD[i+2] not in vowel:
                result = 'not acceptable.'

    # 같은 글자 연속 2번 안된다. ee와 oo는 허용한다.
    for i in range(len(WORD)-1):
        if WORD[i] == WORD[i+1]:
            result = 'not acceptable.'
        if WORD[i] == 'e' and WORD[i+1] == 'e':
            result = 'acceptable.'
        if WORD[i] == 'o' and WORD[i+1] == 'o':
            result = 'acceptable.'

    print('<{}> is {}'.format(WORD, result))




