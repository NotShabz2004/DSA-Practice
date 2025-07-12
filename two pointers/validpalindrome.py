s = "nah"
s = [i.lower() for i in s if i.isalpha() or i.isdigit()]
if (s == s[::-1]):
    print("pal")
else:
    print("nah")
