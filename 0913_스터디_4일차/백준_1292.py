import sys
sys.stdin = open('input_1292.txt', 'r')

# 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5

# 3 3 3 4 4 4 4 5 5 5 5 5 6 6 6 6 6 6 7 7 7 7 7 7 7
# A, B = map(int,input().split())
#
# seq = []
#
# while len(seq) < B:
#     for i in range(1, B):
#         for j in range(0, i):
#             seq.append(i)
#
#
# seqSlice = seq[A-1:B]
#
# print(sum(seqSlice))

START, END = map(int,input().split())

# 1 2 2 3 3 3 4 4 4 4
num_list = []

for i in range(1, 1001):
    for j in range(i):
        num_list.append(i)


result_sum = 0
for i in range(START-1, END):
    result_sum += num_list[i]

print(result_sum)