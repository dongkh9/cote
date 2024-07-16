count=0
while True :
    input_string = input()

    if input_string == '.' :
        break

    check = True
    input_list = list(input_string)
    bracket_list = [ bracket for bracket in input_list if bracket in ( '(', ')', '[', ']' ) ]

    if bracket_list :
        bracket_stack = [bracket_list[0]]

        for i in range(1,len(bracket_list)) :

            if bracket_stack :
                now_bracket = bracket_stack[-1]
            else :
                now_bracket = 0

            if now_bracket == '(' and bracket_list[i] == ')' :
                bracket_stack.pop()

            elif now_bracket == '(' and bracket_list[i] in ( '(' , '[' ) :
                bracket_stack.append(bracket_list[i])

            elif now_bracket == '[' and bracket_list[i] == ']' :
                bracket_stack.pop()

            elif now_bracket == '[' and bracket_list[i] in ( '(' , '[' ) :
                bracket_stack.append(bracket_list[i])

            elif now_bracket == 0 and bracket_list[i] in ( '(' , '[' ) :
                bracket_stack.append(bracket_list[i])

            else :
                check = False
                break
    else :
        bracket_stack = []
    if check and not bracket_stack :
        print('yes')
    else :
        print('no')