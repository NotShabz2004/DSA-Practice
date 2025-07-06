# Intersection of two arrays 1.

"""
https://leetcode.com/problems/intersection-of-two-arrays/description/

Given two integer arrays nums1 and nums2, return an array of their .
Each element in the result must be unique and you may return the result in any order.

My understanding:
Utilizing the advantage whichh sets provide we can easily solve this question.
sets do not allow the same value to be present more than once which makes the process easy.
By iterating the value which is present in the set and the second array we can for a new set with the values
andprint it.
"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        r = set()

        for num in nums2:
            if num in set1:
                r.add(num)

        return (list(r))
