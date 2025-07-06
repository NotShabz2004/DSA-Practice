a = [1, 99, 43, 8, 20, 4]
target = 9
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] + a[j] == target:
            print([i, j])
