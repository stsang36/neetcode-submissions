class Solution:

    
    def isHappy(self, n: int) -> bool:

        seen = dict()

        def helper(n) -> bool:

            if n == 1:
                return True
            
            digits = sum([int(digit)**2 for digit in str(abs(n))])

            if digits in seen:
                return False
            
            if seen.get(digits) is None:
                seen[digits] = True
            
            
            return helper(digits)
            
        
        
        return helper(n)
            

