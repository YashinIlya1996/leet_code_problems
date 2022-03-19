""" https://leetcode.com/problems/maximum-frequency-stack/ """

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
from collections import defaultdict


class FreqStack:

    def __init__(self):
        self.frequency = defaultdict(int)
        self.stack = []

    def push(self, val: int) -> None:
        temp_counter = defaultdict(int)
        self.frequency[val] += 1
        i = -1
        while self.stack and (self.frequency[self.stack[i]] - temp_counter[self.stack[i]] > self.frequency[val]):
            temp_counter[self.stack[i]] += 1
            i -= 1
        if i == -1:
            self.stack.append(val)
        else:
            self.stack.insert(i+1, val)

    def pop(self) -> int:
        el = self.stack.pop()
        self.frequency[el] -= 1
        return el

