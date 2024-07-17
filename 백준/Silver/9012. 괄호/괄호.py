import sys

t = int(sys.stdin.readline())

for _ in range(t) :
    bracket_list = list(sys.stdin.readline().strip())
    bracket_stack = [bracket_list[0]]
    check = True

    for i in range(1,len(bracket_list)) :
        if bracket_stack :
            now_bracket = bracket_stack[-1]
        else :
            now_bracket = ''
        if bracket_list[i] == ')' and now_bracket == '(' :
            bracket_stack.pop()
        elif bracket_list[i] == '(' :
            bracket_stack.append(bracket_list[i])
        else :
            check = False
            break
    if check and not bracket_stack :
        print('YES')
    else :
        print('NO')