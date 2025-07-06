# twosumbrute.py

"""
Problem: Contains Duplicate
LeetCode Link: https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to 
target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

My Understanding:
a normal brute force approach by nesting 2 for loops so we can iterate through the list with 2 indice and 
once we find the perfect pair of number which add up to the target we print their index.
Time Complexity: O(n^2)
Space Complexity: O(1)
Very time consuming. Averaged at 1764 ms.
"""
a = [1, 99, 43, 8, 20, 4]
target = 9
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] + a[j] == target:
            print([i, j])
