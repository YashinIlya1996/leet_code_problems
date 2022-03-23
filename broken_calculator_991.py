"""https://leetcode.com/problems/broken-calculator/"""


class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        if target <= startValue:
            return startValue - target

        answer = 0
        while target != startValue:
            if target < startValue:
                answer += startValue - target
                break
            elif target % 2:
                answer += 2
                target = (target + 1) // 2
            else:
                target //= 2
                answer += 1
        return answer
