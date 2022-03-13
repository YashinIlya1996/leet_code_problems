class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_dict = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        for char in s:
            if char not in brackets_dict:
                stack.append(char)
            else:
                if not stack or stack and stack.pop() != brackets_dict[char]:
                    return False
        if not stack:
            return True
        return False