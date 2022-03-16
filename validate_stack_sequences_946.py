from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = [pushed.pop(0)]
        for pop_el in popped:
            if stack and stack[-1] == pop_el:
                del stack[-1]
            elif pushed:
                while pop_el != (new_stack_el := pushed.pop(0)):
                    stack.append(new_stack_el)
                    if not pushed:
                        break
            else:
                return False
        return True

