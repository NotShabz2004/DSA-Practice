# containsDuplicate.py

"""
Problem: Contains Duplicate
LeetCode Link: https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# Sample test
if __name__ == "__main__":
    solution = Solution()
    test_input = [1, 2, 3, 4, 1]
    print(solution.containsDuplicate(test_input))  # Output: True
