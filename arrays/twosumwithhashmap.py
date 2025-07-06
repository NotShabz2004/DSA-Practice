s = [1, 2, 3, 4]
target = 7
r = {}

for i in range(len(s)):
    needed = target - s[i]
    if needed in r:
        print([r[needed], i])  # Indices that sum to target
        break
    r[s[i]] = i  # store number as key, index as value
