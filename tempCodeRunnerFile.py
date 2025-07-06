a = "leetcode"
r = {}
for m in a:
    r[m] = r.get(m, 0)+1

for i in range(len(a)):
    if r[a[i]] == 1:
        print(i)
else:
    print(0)
