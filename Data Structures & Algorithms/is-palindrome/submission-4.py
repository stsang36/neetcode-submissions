class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        san = list()

        for c in s:
            if c.isalnum():
                san.append(c.lower())

        n = len(san)

        for i in range(n//2):

            if san[i] != san[n - i - 1]:
                
                return False
        
        return True
