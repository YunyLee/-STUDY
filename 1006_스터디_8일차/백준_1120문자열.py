import sys
sys.stdin = open('input_1120.txt', 'r')

# 브루트 포스...

A, B = input().split()

result_cnt = []
N = len(B)
M = len(A)
for i in range(N - M + 1): #구간합!
    cnt = 0
    for j in range(M): # A의 길이만큼만 비교해주면 됨!
        if A[j] != B[i + j]:
            cnt += 1
    result_cnt.append(cnt)

print(min(result_cnt)) #어차피 최소로 다른값을 찾아야되기 때문에 앞뒤 붙이는거 고려안해줘도된다.


# A, B = list(input().split())
# cnt = 0
# while len(A) < len(B):
#     max_diff = 0
#     num = 0
#     # A와 B의 길이가 같을때
#     if len(A) == len(B):
#         for i in len(A):
#             if A[i] != B[i]:
#                 cnt += 1
#                 break
#
#     elif len(A) < len(B):
#         for i in range(len(B) - len(A)+1):
#             for j in range(len(A)):
#                 temp = 0
#                 if B[i:i+len(A)][j] != A[j]:
#                     temp += 1
#                 if temp > max_diff:
#                     max_diff = temp
#                     num = i
#         if num != 0:
#             A = B[0] + A
#         else:
#             A = A + B[-1]
# print(cnt)


#실패 코드들

# while len(A)<len(B):
#     if B[1] == A[0] and B[-2] != A[-1]:
#         A = B[0] + A
#     elif B[1] != A[0] and B[-2] == A[-1]:
#         A = A + B[-1]
#
# for i in range(len(B)):
#     if A[i] != B[i]:
#         cnt += 1
#
# print(cnt)


# A_cnt_dict = dict()
# B_cnt_dict = dict()
#
# for i in A:
#     if i not in A_cnt_dict.keys():
#         A_cnt_dict[i] = 1
#     else:
#         A_cnt_dict[i] += 1
#
# for j in B:
#     if j not in B_cnt_dict.keys():
#         B_cnt_dict[j] = 1
#     else:
#         B_cnt_dict[j] += 1
