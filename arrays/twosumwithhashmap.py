# s = [1, 2, 3, 4]
# target = 7
# r = {}
# for i in range(len(s)):
#     need = target-s[i]
#     if need in r:
#         print([r(need), i])
#     r[s[i]] = i

# intersection of arrays

# nums1 = [4, 9, 5]
# nums2 = [9, 4, 9, 8, 4]
# a = {}
# k = []
# for i in nums1:
#     a[i] = a.get(i, 0)+1
# for j in nums2:
#     if j in a and a[j] > 0:
#         k.append(j)
#         a[j] -= 1
# print(k)

# top k elements
# nums = [29, 88, 44, 9, 1, 29, 29, 5, 77, 88]
# k = 3
# a = {}
# for i in nums:
#     a[i] = a.get(i, 0)+1
# j = sorted(a.items(), key=lambda x: x[1], reverse=True)
# for m in range(k):
#     print(j[m][0])

a = {1: 20, 3: 40, 5: 60}
print(a[1])
