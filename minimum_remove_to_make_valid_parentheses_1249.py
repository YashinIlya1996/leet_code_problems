def remove_parentheses(s: str) -> str:
    answer = ''
    stack = []
    alone_pars = 0
    for num, char in enumerate(s):
        if char != ')' and char != '(':
            answer += char
        elif char == '(':
            if s[num + 1:].count(')') > alone_pars:
                alone_pars += 1
                answer += char
                stack.append('(')

        else:
            if stack and stack[-1] == '(':
                answer += char
                del stack[-1]
                if alone_pars:
                    alone_pars -= 1

    return answer


for _ in range(10):
    print(remove_parentheses(input()))
