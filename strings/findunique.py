# firstUniqChar.py

"""
Problem: First Unique Character in a String
LeetCode Link: https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string s, find the first non-repeating character in it and return its index.
If it does not exist, return -1.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        r = {}

        for char in s:
            r[char] = r.get(char, 0) + 1

        for i in range(len(s)):
            if r[s[i]] == 1:
                return i

        return -1


# Sample test
if __name__ == "__main__":
    solution = Solution()
    input_str = "leetcode"
    result = solution.firstUniqChar(input_str)
    print(f"First unique character index in '{input_str}' is: {result}")
