class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)

        if n == 0:
            return 0

        maxLen = 1

        window = set()
        left = 0
        window.add(s[left])

        for right in range(1, n):

            while s[right] in window:
                window.remove(s[left])
                left += 1
            
            window.add(s[right])
            maxLen = max(maxLen, right - left + 1)

        

        return maxLen

        