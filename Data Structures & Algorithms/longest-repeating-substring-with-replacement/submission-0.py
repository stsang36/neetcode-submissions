class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        n = len(s)

        maxf = 0
        left = 0

        window = set()
        count = dict()

        res = 0 
        for right in range(n):

            count[s[right]] = 1 + count.get(s[right], 0)
            maxf = max(maxf, count.get(s[right]))

            while (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res







        