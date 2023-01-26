

word = int(input())
for i in range(word):
    a = input()
    stack = []
    for x in a:
        if stack:
            if x == '(':

                stack.append(a)

            elif a == ')':
                if stack[-1] == '(':
                    stack.pop()
                
                else:
                    stack.append(a)
    
        else:
            stack.append(a)
        
    if stack:
        print("NO")
    else:
        print('YES')
