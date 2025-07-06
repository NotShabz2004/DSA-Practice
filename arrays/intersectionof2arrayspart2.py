"""_summary_

    Given two integer arrays nums1 and nums2, return an array of their intersection. 
    Each element in the result must appear as many times as it shows in 
    both arrays and you may return the result in any order.

    My understanding:
    just if statement to check if the value exist, if it does we decrease the valuein dictionary and update it in the list
    """


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r = {}
        result = []
        for i in nums1:
            r[i] = r.get(i, 0)+1
        for m in nums2:
            if r.get(m, 0) > 0:
                result.append(m)
                r[m] -= 1
        return result
