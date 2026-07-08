class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        d = dict()
        d2 = dict()

        for l in s:

            if d.get(l) is None:
                d[l] = 0
            else:
                d[l] += 1
        
        for l in t:
            if d2.get(l) is None:
                d2[l] = 0
            else:
                d2[l] += 1
        
        if d == d2:
            return True
        return False
        