nums = [0, 1, 0, 3, 12]
l = 0
for r in range(len(nums)):
    if nums[r] != 0:
        temp = nums[l]
        nums[l] = nums[r]
        nums[r] = temp
        l += 1
print(nums)
