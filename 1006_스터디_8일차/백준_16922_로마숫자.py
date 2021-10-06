import sys
sys.stdin = open('input_16922.txt', 'r')

N = int(input())
sum_list = []
# I : 1 V : 5 X : 10 L : 50

for I in range(N+1): # I를 기준으로 I가 N글자 중 '0'없을수도 '1' 1개 있을수도 '2' 2개 있을수도
    for V in range(N+1-I): # I가 포함된 개수만큼은 빼주자!
        for X in range(N+1-I-V): # I 포함된 개수 그리고 V 포함된 개수만큼 빼자
            L = N - I - V - X # 마지막 L은 N글자 중 I랑 V랑 X랑 몇개인지 이미 차지한 개수만큼 빼줘야 한다.
            num = 1*I + 5*V + 10*X + 50*L
            if num not in sum_list:
                sum_list.append(num)

print(len(sum_list)) # sum_list의 길이라는 말은 중복되지 않은 num조합의 개수!

# '1자리 - 4'
# 1
# 2
# 3
# 4
#
# '2자리 - 10'
# 11 12 13 14
# 22 23 24
# 33 34
# 44
#
#
# '3자리 - 20'
# 111 112 113 114
# 122 123 124
# 133 134
# 144
#
# 222 223 224
# 233 234
# 244
#
# 333 334
# 344
#
# 444

