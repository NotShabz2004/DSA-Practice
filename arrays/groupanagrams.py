from collections import defaultdict
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
grp = defaultdict(list)
for i in strs:
    k = tuple(sorted(i))
    grp[k].append(i)
print(list(grp.values()))
