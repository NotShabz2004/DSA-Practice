# # Given an integer array nums, return true if any value appears at least twice in the array,
# # and return false if every element is distinct.

# s = [1, 2, 2, 1]
# r = [2, 2]
# a = set(s)
# j = set()
# for i in r:
#     if i in a:
#         j.add(i)
# print(j)

# Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# s = "anagram"
# t = "raw"
# a = len(s)
# b = len(t)
# if a != b:
#     print("False")
# freq = {}
# for i in s:
#     freq[i] = freq.get(i, 0)+1

# for j in t:
#     if j in freq:
#         freq[j] -= 1
#         if freq[j] < 0:
#             print("False")
#     else:
#         print("False")
# else:
#     print("True")

# Two Sum(Bruteforce)
# a = [2, 7, 11, 15]
# t = 9
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         if a[i]+a[j] == t:
#             print([i, j])
# else:
#     print("False")

# Two sum Hashmap
# a = [2, 7, 11, 15]
# t = 9
# j = {}
# for i in a:
#     if t-i in j:
#         print(j[i], i)
#     j += i
from collections import defaultdict
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

grp = defaultdict(list)


for i in strs:
    k = tuple(sorted(i))
    print(k)
    grp[k].append(i)
print(grp)
