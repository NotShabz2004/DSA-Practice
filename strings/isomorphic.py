s = "egge"
t = "addg"
a = {}
b = {}
if len(s) != len(t):
    print("False")

for i in range(len(s)):
    e = s[i]
    f = t[i]
    if e in a and a[e] != f:
        print("False")
    if f in a and b[f] != e:
        print("False")
else:
    print("True")
