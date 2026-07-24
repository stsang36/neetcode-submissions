class Solution:

    def getHash(self, s: str) -> str:
        res = []
        h = [0] * 26

        for c in s:
            h[ord(c) - ord('a')] += 1

        for i in range(26):
            res.append(str(h[i]))
            res.append("$")

        return ''.join(res)



    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for s in strs:
            k = self.getHash(s)

            if mp.get(k) is None:
                mp[k] = []
                mp[k].append(s)
            else:
                mp[k].append(s)
        
        return list(mp.values())