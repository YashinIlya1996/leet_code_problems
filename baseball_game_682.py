""" https://leetcode.com/problems/baseball-game/ """
from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        score = []
        COMMANDS = {
            "+": lambda: score.append(score[-1] + score[-2]),
            "D": lambda: score.append(2 * score[-1]),
            "C": lambda: score.pop(),
        }

        def execute_command(command: str):
            if command.lstrip("-").isdigit():
                score.append(int(command))
            else:
                COMMANDS[command]()

        for command in ops:
            execute_command(command)

        return sum(score)
