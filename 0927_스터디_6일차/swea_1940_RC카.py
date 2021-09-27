import sys
sys.stdin = open('input_1940.txt', 'r')

# 가랏! RC카!

TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    command_list = []
    speed_list = []
    now_speed = 0
    cnt = 0
    for i in range(N):
        temp = input()
        if temp != '0':
            COMMAND, SPEED = temp.split()
            command_list.append(COMMAND)
            speed_list.append(SPEED)
        else:
            SPEED = 0
            command_list.append('0')
            speed_list.append('0')

    for i in range(len(command_list)):
        if command_list[i] == '1':
            now_speed += int(speed_list[i])
            cnt += now_speed
        elif command_list[i] == '2':
            if int(speed_list[i]) <= now_speed:
                now_speed -= int(speed_list[i])
                cnt += now_speed
            else:
                now_speed = 0
        elif command_list[i] == '0':
            now_speed += 0
            cnt += now_speed

    print('#{} {}'.format(test_case, cnt))