import sys
sys.stdin = open('input_2941.txt', 'r')

TC = int(input())

for test_case in range(1, TC+1):
    WORD = input()
    croatia_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    result = WORD


    for i in croatia_alphabet:
        result = result.replace(i, 'p')
    print(len(result))




    # result = 0
    # my_cnt = 0
    # my_len = 0

    # croatia_alphabet = ['c=','c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    #
    # for i in range(len(croatia_alphabet)):
    #     if croatia_alphabet[i] in WORD:
    #         my_len = 0
    #         my_cnt = 0
    #         for j in croatia_alphabet[i]:
    #             WORD.remove(croatia_alphabet[i][j])
    #         my_cnt += 1
    #         my_len += len(croatia_alphabet[i])
    #
    #         result = my_cnt + len(WORD) - my_len
    #
    # print(result)

    #

    #         for i in WORD:
    #             if croatia_alphabet[j][k] == i:
    #                 my_cnt += 1
    #             if my_cnt == len(croatia_alphabet[j]):
    #                 result += 1
    #                 my_cnt = 0
    #                 break
