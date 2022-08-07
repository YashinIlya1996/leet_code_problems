""" https://leetcode.com/problems/count-vowels-permutation/ """
from collections import Counter


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10 ** 9 + 7
        next_possible_letters = {'a': 'e', 'e': 'ai', 'i': 'uoea', 'o': 'iu', 'u': 'a'}
        all_possible_letters = 'aueio'
        total_count = 5
        previous_step_letter_counter = Counter(all_possible_letters)
        step_letter_counter = Counter()
        for _ in range(1, n):
            for letter, prev_letter_count in previous_step_letter_counter.items():
                d = {l: prev_letter_count for l in next_possible_letters[letter]}
                step_letter_counter.update(d)
            total_count = sum(step_letter_counter.values())
            previous_step_letter_counter, step_letter_counter = step_letter_counter, Counter()

        return total_count % mod


if __name__ == '__main__':
    print(Solution().countVowelPermutation(5))
