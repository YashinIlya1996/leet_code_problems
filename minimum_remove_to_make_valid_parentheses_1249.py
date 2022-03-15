class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        answer = ''
        stack = []  # Стэк для проверки того, что перед закрывающей скобкой есть парная открывающая
        alone_pars = 0
        count_sad = 0
        all_count_sad = s.count(')')
        for num, char in enumerate(s):
            if char != ')' and char != '(':
                answer += char
            elif char == '(':
                # Открывающая скобка добавляется только в том случае, 
                # если в строке еще имеется соответствующая закрывающая скобка
                if all_count_sad - count_sad > alone_pars: 
                    alone_pars += 1
                    answer += char
                    stack.append('(')
            else:
                # Проверка на то, что перед закрывающей скобкой была свободная открывающая
                # тем самым отсекаются выражения вида *(*)*)*
                if stack and stack[-1] == '(':
                    answer += char
                    del stack[-1]
                    if alone_pars:
                        alone_pars -= 1
                count_sad += 1
        return answer