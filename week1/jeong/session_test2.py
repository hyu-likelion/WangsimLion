def solution(new_id):
    id = list(new_id)
    stack = []
    stacknum = 0

    for c in id:
        if c.isalnum(): #영어또는숫자
            c.lower()
            stack.append(c)
            stacknum += 1
        else:
            if c == ".":
                if stacknum == 0:
                    pass
                elif stack[stacknum-1] == ".":
                    pass
                else:
                    stack.append(c)
                    stacknum += 1
            elif c == "-":
                stack.append(c)
                stacknum += 1
                
            elif c == "_":
                stack.append(c)
                stacknum += 1
            else:
                newc = ."
                if stacknum == 0:
                    pass
                elif stack[stacknum-1] == ".":
                    pass
                else:
                    stack.append(newc)
                    stacknum += 1
    if stacknum == 0:
        stack.append("a")
    elif stacknum >= 16:
        while stacknum == 15:
            stack.pop()
            stacknum -= 1
        if stack[stacknum-1] == ".":
            stack.pop()
            stacknum -= 1
    elif stacknum <=2:
        while stacknum == 3:
            temp = stack.pop()
            stacknum -= 1
            stack.append(temp)
            stack.append(temp)
            stacknum += 2
    result = ''.join(stack)
    return result
        

solution("aaa")