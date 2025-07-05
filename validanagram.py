class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = len(s)
        b = len(t)
        if a != b:
            return False
        freq = {}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for m in t:
            if m in freq:
                freq[m] -= 1
                if freq[m] < 0:
                    return False
            else:
                return False
        return True
